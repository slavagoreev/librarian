from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..permissions import permission_0, permission_2, permission_3, permission_1
from .orders_serializers import OrderSerializer, OrderDetailSerializer
from ..tg_bot.engine import send_message
from ..models import Order, User, Document
from .. import const

from threading import Thread
import datetime
import time

DEFAULT_SIZE = 15
DEFAULT_OFFSET = 0


class Orders(APIView):
    """
        Class to get all orders
    """

    @staticmethod
    @permission_1
    def get(request):
        """
        Return set of all orders
        :param request:
        :return: HTTP_200_OK and JSON
        """

        size = request.GET.get('size', None)
        offset = request.GET.get('offset', None)

        result = {'status': '', 'data': {}}

        start = int(offset if offset else DEFAULT_OFFSET)
        finish = int(offset if offset else DEFAULT_OFFSET) + int(size if size else DEFAULT_SIZE)
        orders = OrderDetailSerializer(Order.objects.exclude(copy=None), many=True)[start:finish]

        result['data'] = orders.data

        return Response(result, status=status.HTTP_200_OK)


class OrdersQueue(APIView):
    """
        Class to get orders in queue order
    """

    @staticmethod
    @permission_1
    def get(request):
        """
        Return set of orders in queue
        :param request:
        :return: HTTP_200_OK and JSON
        """

        size = request.GET.get('size', None)
        offset = request.GET.get('offset', None)

        result = {'status': '', 'data': {}}

        start = int(offset if offset else DEFAULT_OFFSET)
        finish = int(offset if offset else DEFAULT_OFFSET) + int(size if size else DEFAULT_SIZE)
        orders_in_queue = OrderDetailSerializer(Order.get_queue(), many=True)[start:finish]

        result['data'] = orders_in_queue.data

        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    @permission_2
    def delete(request, document_id):
        """
        Outstanding request for the document
        :param document_id: document to request
        :return:
        """
        result = {'status': '', 'data': {}}

        try:
            document = Document.objects.get(document_id=document_id)

            Order.outstanding_request(document)

        except Document.DoesNotExist:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        return Response(result, status=status.HTTP_200_OK)


class OrderDetail(APIView):
    """
        Class to react with orders
    """

    @staticmethod
    @permission_1
    def get(request, order_id):

        result = {'status': '', 'data': {}}

        try:
            orders = OrderDetailSerializer(Order.objects.get(order_id=order_id))

            result['data'] = orders.data

            return Response(result, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    @permission_1
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
                    return Response(result, status=status.HTTP_404_NOT_FOUND)

                order.accept_booking()

                return Response(result, status=status.HTTP_200_OK)

            elif new_status == const.CLOSED_STATUS and old_status != const.CLOSED_STATUS:

                overdue_sum = order.close()
                result['data'] = {'overdue_sum': overdue_sum}
                return Response(result, status=status.HTTP_200_OK)

            else:

                # if status nor 1 or 3 than it is incorrect request
                result['data'] = 'no such option'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

        except Order.DoesNotExist:
            result['data'] = 'order dose not exist'
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            result['data'] = 'incorrect data was provided'
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

        size = request.GET.get('size', None)
        offset = request.GET.get('offset', None)

        result = {'status': '', 'data': {}}

        user = User.get_instance(request=request)

        start = int(offset if offset else DEFAULT_OFFSET)
        finish = int(offset if offset else DEFAULT_OFFSET) + int(size if size else DEFAULT_SIZE)
        orders = OrderDetailSerializer(Order.objects.filter(user=user), many=True)[start:finish]

        result['data'] = orders.data
        return Response(result, status=status.HTTP_200_OK)


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
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            document = Document.objects.get(pk=document_id)
            orders = Order.objects.all().filter(user=User.get_instance(request))

            for order in orders:
                if order.document.document_id == document.document_id and (order.status == const.IN_QUEUE_STATUS or
                                                                           order.status == const.BOOKED_STATUS or
                                                                           order.status == const.OVERDUE_STATUS):
                    result['data'] = {'details': 'you already booked this document'}
                    return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if document.is_reference:
                result['data'] = {'details': 'reference document cannot be checked out'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            order = Order.objects.create(
                document=document,
                user=user
            )

            order_serializer = OrderSerializer(order)
            result['data'] = order_serializer.data
            return Response(result, status=status.HTTP_200_OK)

        except IndexError:

            return Response(result, status=status.HTTP_404_NOT_FOUND)

        except Document.DoesNotExist or User.DoesNotExist:

            return Response(result, status=status.HTTP_404_NOT_FOUND)

        finally:
            if order:
                def f():
                    order.attach_copy()
                    if not order.copy:
                        msg = "Dear " + order.user.first_name + ",\n\nWhen the document " + \
                              order.document.title + " will be available for checkout " \
                                                    "you will be notified."

                        send_message(order.user.telegram_id, msg)
                    print('sended')

                Thread(target=f).start()


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
            time.sleep(datetime.timedelta(minutes=60).seconds)


MyThread().start()
