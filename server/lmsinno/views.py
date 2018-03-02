import datetime

from django.utils.datastructures import MultiValueDictKeyError

from .permissions import DocumentPermission, LibrariantPermission, AuthenticatedUserPermission, UserDetailPermission
from .models import Document, Author, DocumentOfAuthor, Tag, TagOfDocument, User, Order, Copy
from .serializer import  UserSerializer, OrderSerializer, UserSafeSerializer, \
    UserResponceDataSerializer, UserDetailSerializer, OrderDetailSerializer

from rest_framework.response import Response
from rest_framework import status, serializers, response, schemas
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import detail_route, permission_classes, api_view, renderer_classes
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from .misc import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, \
    HTTP_409_CONFLICT, HTTP_401_UNAUTHORIZED

import re
import base64


# schema_view = get_swagger_view(title='Librarian API Docs')

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='REST API')
    return response.Response(generator.get_schema())


class Users(APIView):
    """
       Class to get list of all Users
    """
    permission_classes = (LibrariantPermission,)

    @staticmethod
    def get(request):
        """
            GET request to get list of all Users
            :param request:
            :return: HTTP_200_OK and JSON-Documents: if all good
                     HTTP_404_NOT_FOUND: if users don`t exist
        """
        result = {'status': '', 'data': {}}

        if not User.objects.all():
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserResponceDataSerializer(User.objects.all(), many=True)
        result['data'] = serializer.data
        result['status'] = HTTP_200_OK

        return Response(result, status=status.HTTP_200_OK)


class UserDetail(APIView):
    """
        Class to get one User by id
    """
    permission_classes = (UserDetailPermission,)

    @staticmethod
    def get(request, user_id):
        """
            GET request to get one particular user
            :param request:
            :param user_id
            :return: HTTP_200_OK and JSON-Documents: if all good
                    HTTP_404_NOT_FOUND: if user don`t exist
        """
        result = {'status': '', 'data': {}}

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user)
        result['data'] = serializer.data
        result['status'] = HTTP_200_OK
        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def patch(request, user_id):
        """
            PATCH request to update users
            :param request:
            :param user_id:
            :return: HTTP_202_ACCEPTED and JSON-Document: update is success
                     HTTP_400_BAD_REQUEST and JSON-Document with errors: data is not valid
                     HTTP_404_NOT_FOUND: user with such id is not found
        """

        result = {'status': '', 'data': {}}

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            # First, need to check whether the user try to change his role
            # We return 'accepted' in case that 'hacker' who try to change state
            # Might try several times before he totally burn in tears about our security :)
            # NOTE: User.get_instance(request).role - the instance of requester
            if User.get_instance(request).role != 2 and user.role != User.get_instance(request).role:
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            # If pass, then save all
            serializer.save()
            result['status'] = HTTP_202_ACCEPTED
            return Response(result, status=status.HTTP_202_ACCEPTED)

        result['status'] = HTTP_400_BAD_REQUEST
        result['data'] = serializer.errors

        return Response(result, status=status.HTTP_400_BAD_REQUEST)


class MyDetail(APIView):
    """
        Class to get one User by id
    """
    permission_classes = (LibrariantPermission,)

    @staticmethod
    def get(request, user_id):
        """
            GET request to get one particular user
            :param request:
            :param user_id:
            :return: HTTP_200_OK and JSON-Documents: if all good
                    HTTP_404_NOT_FOUND: if user don`t exist
        """
        result = {'status': '', 'data': {}}

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user)
        result['data'] = serializer.data
        result['status'] = HTTP_200_OK
        return Response(result, status=status.HTTP_200_OK)











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
            result['status'] = HTTP_404_NOT_FOUND
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
                if old_order == 1:
                    order.date_return = datetime.date.today()

                order.copy.status = 0
                order.copy.save()
                order.copy.document.copies_available += 1
                order.copy.document.save()

            elif order.status == 0:

                result['status'] = HTTP_400_BAD_REQUEST
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            order.save()

            result['status'] = HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            result['status'] = HTTP_400_BAD_REQUEST
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

        orders = OrderSerializer(Order.objects.filter(user=user), many=True)

        result['data'] = orders.data
        result['status'] = HTTP_200_OK
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

            new_status = int(request.META['HTTP_STATUS'])
            if new_status != 4 or order.status == 4 or order.copy.document.is_bestseller:
                raise KeyError

            delta = datetime.timedelta(weeks=1)
            order.date_return += delta
            order.status = new_status
            order.save()

            result['status'] = HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            result['status'] = HTTP_400_BAD_REQUEST
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

            if document.copies_available == 0:
                result['status'] = HTTP_400_BAD_REQUEST
                result['data'] = {'details': 'document is not available (run out of copies)'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            elif document.is_reference:
                result['status'] = HTTP_400_BAD_REQUEST
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

            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        except Document.DoesNotExist:

            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        document.copies_available -= 1
        document.save()

        order_serializer = OrderSerializer(order)
        result['data'] = order_serializer.data
        result['status'] = HTTP_200_OK

        return Response(result, status=status.HTTP_200_OK)
