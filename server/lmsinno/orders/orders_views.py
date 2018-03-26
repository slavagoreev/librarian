from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .orders_serializers import OrderSerializer, OrderDetailSerializer
from ..permissions import LibrariantPermission
from ..models import Order, User, Document, Copy
from .. import misc


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
        Order.overdue_and_queue_validation()
        result = {'status': '', 'data': {}}

        orders = OrderDetailSerializer(Order.objects.all().exclude(copy=None), many=True)

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
        Order.overdue_and_queue_validation()
        result = {'status': '', 'data': {}}

        orders_in_queue = OrderDetailSerializer(Order.get_queue(), many=True)

        result['data'] = orders_in_queue.data

        return Response(result, status=status.HTTP_200_OK)


class OrderDetail(APIView):
    permission_classes = (LibrariantPermission,)
    """
        Class to react with orders
    """

    @staticmethod
    def get(request, order_id):
        Order.overdue_and_queue_validation()
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
        Order.overdue_and_queue_validation()
        result = {'status': '', 'data': {}}

        try:

            order = Order.objects.get(order_id=order_id)
            document = order.document

            old_status = int(order.status)
            new_status = int(request.data['status'])

            # if new status is BOOKED_STATUS or CLOSED_STATUS proceed
            if new_status == misc.BOOKED_STATUS and old_status == misc.IN_QUEUE_STATUS:

                if document.copies_available == 0 and not order.copy:
                    result['data'] = 'no copy available'
                    result['status'] = misc.HTTP_404_NOT_FOUND
                    return Response(result, status=status.HTTP_404_NOT_FOUND)

                order.accept()

                result['status'] = misc.HTTP_200_OK
                return Response(result, status=status.HTTP_200_OK)

            elif new_status == misc.CLOSED_STATUS and old_status != misc.CLOSED_STATUS:

                overdue_sum = order.close()
                result['data'] = {'overdue_sum': overdue_sum}
                result['status'] = misc.HTTP_200_OK
                return Response(result, status=status.HTTP_200_OK)

            else:

                # if status nor 1 or 3 than it is incorrect request
                result['data'] = 'no such option'
                result['status'] = misc.HTTP_400_BAD_REQUEST
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

        except Order.DoesNotExist:
            result['data'] = 'order dose not exist'
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            result['data'] = 'incorrect data was provided'
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
        Order.overdue_and_queue_validation()
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
            my_order = Order.objects.get(order_id=order_id)
            document = my_order.copy.document

            if my_order.user != User.get_instance(request=request):
                raise KeyError

            new_status = int(request.data['status'])
            if new_status != 4:
                raise KeyError

            # Visiting Professor patron can renew an item as many times as he wants
            if my_order.status == 4 and my_order.user.role != misc.VISITING_PROFESSOR_ROLE:
                raise KeyError

            # TODO renew item

            if document.copies_available == 0:
                orders = Order.objects.filter(status=0)
                for order in orders:
                    if order.document == document:
                        raise LookupError

            my_order.extend()

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
                user=user
            )

            order.attach_copy()

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
