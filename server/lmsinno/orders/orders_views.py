from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .orders_serializers import OrderSerializer, OrderDetailSerializer
from ..permissions import LibrariantPermission
from ..models import Order, User, Document, Copy
from .. import misc

import datetime


class Orders(APIView):
    permission_classes = (LibrariantPermission,)
    """
        Class to get all orders
    """

    @staticmethod
    def get(request):
        """
        Return set of all orders
        :param request:
        :return: HTTP_200_OK and JSON
        """
        Order.overdue_validation()
        result = {'status': '', 'data': {}}

        orders = OrderDetailSerializer(Order.objects.all(), many=True)

        result['data'] = orders.data

        return Response(result, status=status.HTTP_200_OK)


class OrdersQueue(APIView):
    permission_classes = (LibrariantPermission,)
    """
        Class to get orders in queue order
    """

    @staticmethod
    def get(request):
        """
        Return set of orders in queue
        :param request:
        :return: HTTP_200_OK and JSON
        """
        Order.overdue_validation()
        result = {'status': '', 'data': {}}

        # get clean queue of orders
        orders_in_queue = Order.objects.filter(status=0)

        # TODO priority queue for orders

        orders_in_queue = orders_in_queue.order_by('-user__role')
        orders_in_queue = orders_in_queue.reverse()[::-1]
        # orders_in_queue = list(orders_in_queue)

        orders_in_queue = OrderDetailSerializer(orders_in_queue, many=True)

        result['data'] = orders_in_queue.data

        return Response(result, status=status.HTTP_200_OK)


class OrderDetail(APIView):
    permission_classes = (LibrariantPermission,)
    """
        Class to react with orders
    """

    @staticmethod
    def get(request, order_id):
        Order.overdue_validation()
        result = {'status': '', 'data': {}}

        try:
            orders = OrderDetailSerializer(Order.objects.get(order_id=order_id))

            result['data'] = orders.data

            return Response(result, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def patch(request, order_id):
        """
        Check out one order for document
        :param request:
        :param order_id:
        :return: HTTP_404_NOT_FOUND:
            if no copy available for this order
        :return: HTTP_200_OK and JSON
        """
        Order.overdue_validation()
        result = {'status': '', 'data': {}}

        try:

            order = Order.objects.get(order_id=order_id)
            document = order.document

            old_status = int(order.status)
            new_status = int(request.data['status'])

            # if order status is 1 or 3 proceed
            # we can accept closed orders just because
            if new_status == 1 and old_status == 0:
                if document.copies_available == 0 and not order.copy:
                    result['data'] = 'no copy available'
                    result['status'] = misc.HTTP_404_NOT_FOUND
                    return Response(result, status=status.HTTP_404_NOT_FOUND)

                order.copy = document.get_copy()

                order.date_accepted = datetime.date.today()

                if order.user.role == 0:
                    delta = datetime.timedelta(weeks=3)
                    order.date_return = datetime.date.today() + delta

                if order.copy.document.is_bestseller:
                    delta = datetime.timedelta(weeks=2)
                    order.date_return = datetime.date.today() + delta

                if order.user.role >= 1:
                    delta = datetime.timedelta(weeks=4)
                    order.date_return = datetime.date.today() + delta

                if order.copy.document.type > 0:
                    delta = datetime.timedelta(weeks=2)
                    order.date_return = datetime.date.today() + delta

                # Visiting Professor - limit is 1 week (regardless the type of the document)
                if order.user.role == 1.3:
                    delta = datetime.timedelta(weeks=1)
                    order.date_return = datetime.date.today() + delta

            elif new_status == 3:

                if old_status == 2:
                    overdue_days = (datetime.date.today() - order.date_return).days
                    sum = min(overdue_days * 100, order.copy.document.price)
                    result['data'] = {'overdue_sum': sum}
                    order.date_return = datetime.date.today()
                if old_status == 1 or old_status == 4:
                    order.date_return = datetime.date.today()

                # if order closed immediately copies number must no change
                if old_status == 1 or old_status == 2 or old_status == 4:
                    document.return_copy(order.copy)

            else:
                # if status nor 1 or 3 than it is incorrect request
                result['status'] = misc.HTTP_400_BAD_REQUEST
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if 0 < new_status < 5:
                order.status = new_status
                order.save()
            else:
                while 1:
                    print("If reaches this manage to /server/lmsinno/orders/orders_views.py")

            result['status'] = misc.HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            result['data'] = 'order dose not exist'
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            result['status'] = misc.HTTP_400_BAD_REQUEST
            return Response(result, status=status.HTTP_400_BAD_REQUEST)


class MyOrders(APIView):
    """
        Class to see users orders
    """

    @staticmethod
    def get(request):
        """
        Return set of all orders of one particular user
        :param request:
        :return: HTTP_200_OK and JSON
        """
        Order.overdue_validation()
        result = {'status': '', 'data': {}}

        user = User.get_instance(request=request)

        orders = OrderDetailSerializer(Order.objects.filter(user=user), many=True)

        result['data'] = orders.data
        result['status'] = misc.HTTP_200_OK
        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def patch(request, order_id):
        """
        Extended copy for 1 week
        :param request:
        :param order_id
        :return: HTTP_200_OK and JSON
        """
        result = {'status': '', 'data': {}}

        try:
            order = Order.objects.get(order_id=order_id)
            document = order.copy.document

            if order.user != User.get_instance(request=request):
                raise KeyError

            new_status = int(request.data['status'])
            if new_status != 4:
                raise KeyError

            # Visiting Professor patron can renew an item as many times as he wants
            if order.status == 4 and order.user.role != 1.3:
                raise KeyError

            if document.copies_available == 0:
                orders = Order.objects.filter(status=0)
                for order in orders:
                    if order.copy.document == document:
                        raise LookupError

            delta = datetime.timedelta(weeks=1)
            order.date_return += delta
            order.status = new_status
            order.save()

            result['status'] = misc.HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            result['status'] = misc.HTTP_400_BAD_REQUEST
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        except LookupError:
            result['data'] = 'sorry, someone need this book'
            result['status'] = misc.HTTP_400_BAD_REQUEST
            return Response(result, status=status.HTTP_400_BAD_REQUEST)


# TODO copy valid
class Booking(APIView):
    """
    Class to book one particular document by ID
    """

    @staticmethod
    def get(request, document_id):
        """
        Book one particular document by ID
        :param request:
        :param document_id:
        :return: HTTP_200_OK and JSON-order: if tag with such ID exists
                 HTTP_400_BAD_REQUEST and JSON: 'details': 'document is not available'
                 HTTP_400_BAD_REQUEST and JSON: 'details': 'reference document cannot be checked out'
                 HTTP_404_NOT_FOUND and JSON: if document with such id does not exist
        """

        result = {'status': '', 'data': {}}

        try:
            document = Document.objects.get(pk=document_id)
            orders = Order.objects.all().filter(user=User.get_instance(request))

            for order in orders:
                if order.document.document_id == document.document_id:
                    if order.status == 0 or order.status == 1 or order.status == 2 or order.status == 4:
                        result['status'] = misc.HTTP_400_BAD_REQUEST
                        result['data'] = {'details': 'you already booked this document'}
                        return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if document.is_reference:
                result['status'] = misc.HTTP_400_BAD_REQUEST
                result['data'] = {'details': 'reference document cannot be checked out'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            user = User.get_instance(request=request)

            order = Order.objects.create(
                document=document,
                user=user,
            )

        except IndexError:

            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        except Document.DoesNotExist:

            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        order_serializer = OrderSerializer(order)
        result['data'] = order_serializer.data
        result['status'] = misc.HTTP_200_OK

        return Response(result, status=status.HTTP_200_OK)
