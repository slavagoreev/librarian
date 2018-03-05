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
        Order.overdue_validation()
        result = {'status': '', 'data': {}}

        try:
            order = Order.objects.get(order_id=order_id)
            old_order = int(order.status)
            order.status = int(request.data['status'])

            # if order status is 1 or 3 proceed
            if order.status == 1:
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

            elif order.status == 3:

                if old_order == 2:
                    overdue_days = (datetime.date.today() - order.date_return).days
                    sum = min(overdue_days * 100, order.copy.document.price)
                    result['data'] = {'overdue_sum': sum}
                    order.date_return = datetime.date.today()
                if old_order == 1 or old_order == 4:
                    order.date_return = datetime.date.today()

                order.copy.status = 0
                order.copy.save()
                order.copy.document.copies_available += 1
                order.copy.document.save()

            elif order.status == 0:

                result['status'] = misc.HTTP_400_BAD_REQUEST
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            order.save()

            result['status'] = misc.HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
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

            if order.user != User.get_instance(request=request):
                raise KeyError

            new_status = int(request.data['status'])
            if new_status != 4 or order.status == 4 or order.copy.document.is_bestseller:
                raise KeyError

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

            for i in orders:
                if i.copy.document.document_id == document.document_id:
                    if i.status != 3:
                        result['status'] = misc.HTTP_400_BAD_REQUEST
                        result['data'] = {'details': 'you already booked this document'}
                        return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if document.copies_available == 0:
                result['status'] = misc.HTTP_400_BAD_REQUEST
                result['data'] = {'details': 'document is not available (run out of copies)'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            elif document.is_reference:
                result['status'] = misc.HTTP_400_BAD_REQUEST
                result['data'] = {'details': 'reference document cannot be checked out'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            copy = Copy.objects.all()
            copy = copy.filter(document=document)
            copy = copy.filter(status=0)
            copy = copy[0]
            copy.status = 1
            copy.save()

            user = User.get_instance(request=request)

            order = Order.objects.create(
                copy=copy,
                user=user,
            )

        except IndexError:

            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        except Document.DoesNotExist:

            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        document.copies_available -= 1
        document.save()

        order_serializer = OrderSerializer(order)
        result['data'] = order_serializer.data
        result['status'] = misc.HTTP_200_OK

        return Response(result, status=status.HTTP_200_OK)
