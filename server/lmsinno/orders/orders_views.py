from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .orders_serializers import OrderSerializer, OrderDetailSerializer
from ..permissions import LibrariantPermission
from ..models import Order, User, Document, Copy
from .. import const


from threading import Thread
import datetime
import time


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

        result = {'status': '', 'data': {}}

        orders_in_queue = OrderDetailSerializer(Order.get_queue(), many=True)

        result['data'] = orders_in_queue.data

        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, document_id):
        """

        :param request:
        :param document_id:
        :return:
        """
        result = {'status': '', 'data': {}}

        try:
            document = Document.objects.get(document_id=document_id)

            Order.outstanding_request(document)

        except Document.DoesNotExist:
            result['status'] = const.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        result['status'] = const.HTTP_200_OK
        return Response(result, status=status.HTTP_200_OK)


class OrderDetail(APIView):
    permission_classes = (LibrariantPermission,)
    """
        Class to react with orders
    """

    @staticmethod
    def get(request, order_id):

        result = {'status': '', 'data': {}}

        try:
            orders = OrderDetailSerializer(Order.objects.get(order_id=order_id))

            result['data'] = orders.data

            return Response(result, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            result['status'] = const.HTTP_404_NOT_FOUND
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

        result = {'status': '', 'data': {}}

        try:

            order = Order.objects.get(order_id=order_id)
            document = order.document

            old_status = int(order.status)
            new_status = int(request.data['status'])

            # if new status is BOOKED_STATUS or CLOSED_STATUS proceed
            if new_status == const.BOOKED_STATUS and old_status == const.IN_QUEUE_STATUS:

                if document.copies_available == 0 and not order.copy:
                    result['data'] = 'no copy available'
                    result['status'] = const.HTTP_404_NOT_FOUND
                    return Response(result, status=status.HTTP_404_NOT_FOUND)

                order.accept_booking()

                result['status'] = const.HTTP_200_OK
                return Response(result, status=status.HTTP_200_OK)

            elif new_status == const.CLOSED_STATUS and old_status != const.CLOSED_STATUS:

                overdue_sum = order.close()
                result['data'] = {'overdue_sum': overdue_sum}
                result['status'] = const.HTTP_200_OK
                return Response(result, status=status.HTTP_200_OK)

            else:

                # if status nor 1 or 3 than it is incorrect request
                result['data'] = 'no such option'
                result['status'] = const.HTTP_400_BAD_REQUEST
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

        except Order.DoesNotExist:
            result['data'] = 'order dose not exist'
            result['status'] = const.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            result['data'] = 'incorrect data was provided'
            result['status'] = const.HTTP_400_BAD_REQUEST
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

        result = {'status': '', 'data': {}}

        user = User.get_instance(request=request)

        orders = OrderDetailSerializer(Order.objects.filter(user=user), many=True)

        result['data'] = orders.data
        result['status'] = const.HTTP_200_OK
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

            if my_order.user != User.get_instance(request=request):
                raise KeyError

            if not my_order.is_renewable():
                result['data'] = 'sorry, you can not renew this document'
                result['status'] = const.HTTP_400_BAD_REQUEST
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            # TODO renew item

            my_order.renew()

            result['status'] = const.HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            result['status'] = const.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            result['data'] = "sorry, you can renew only your document"
            result['status'] = const.HTTP_400_BAD_REQUEST
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
            user = User.get_instance(request=request)
            if not user.telegram_id:
                result['data'] = 'no telegram id was provided'
                result['status'] = const.HTTP_400_BAD_REQUEST
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            document = Document.objects.get(pk=document_id)
            orders = Order.objects.all().filter(user=User.get_instance(request))

            for order in orders:
                if order.document.document_id == document.document_id and (order.status == const.IN_QUEUE_STATUS or
                                                                           order.status == const.BOOKED_STATUS or
                                                                           order.status == const.OVERDUE_STATUS):
                    result['status'] = const.HTTP_400_BAD_REQUEST
                    result['data'] = {'details': 'you already booked this document'}
                    return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if document.is_reference:
                result['status'] = const.HTTP_400_BAD_REQUEST
                result['data'] = {'details': 'reference document cannot be checked out'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            order = Order.objects.create(
                document=document,
                user=user
            )

            order.attach_copy()

        except IndexError:

            result['status'] = const.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        except Document.DoesNotExist or User.DoesNotExist:

            result['status'] = const.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        order_serializer = OrderSerializer(order)
        result['data'] = order_serializer.data
        result['status'] = const.HTTP_200_OK

        return Response(result, status=status.HTTP_200_OK)


class MyThread(Thread):
    """
    Separate thread for validations
    """
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True

    def run(self):
        Order.overdue_validation()
        Order.queue_overdue_validation()
        while True:
            if 1 >= datetime.datetime.today().time().hour >= 0:
                Order.overdue_validation()
            Order.queue_overdue_validation()
            time.sleep(datetime.timedelta(hours=1).seconds)


MyThread().start()
