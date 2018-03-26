try:
    from rest_auth.registration.views import RegisterView
except ImportError:
    raise ImportError("rest_auth needs to be added to INSTALLED_APPS.")

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .users_serializers import UserResponseDataSerializer, UserDetailSerializer
from ..permissions import LibrariantPermission, UserDetailPermission
from ..models import User
from .. import misc


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
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserResponseDataSerializer(User.objects.all(), many=True)
        result['data'] = serializer.data
        result['status'] = misc.HTTP_200_OK

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
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user)
        result['data'] = serializer.data
        result['status'] = misc.HTTP_200_OK
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
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            # First, need to check whether the user try to change his role
            # We return 'accepted' in case that 'hacker' who try to change state
            # Might try several times before he totally burn in tears about our security :)
            # NOTE: User.get_instance(request).role - the instance of requester
            if User.get_instance(request).role != misc.LIBRARIAN_ROLE:
                return Response(result, status=status.HTTP_202_ACCEPTED)
            # If pass, then save all
            serializer.save()
            result['status'] = misc.HTTP_202_ACCEPTED
            return Response(result, status=status.HTTP_202_ACCEPTED)

        result['status'] = misc.HTTP_400_BAD_REQUEST
        result['data'] = serializer.errors

        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
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
                return Response({'status': misc.HTTP_404_NOT_FOUND, 'data': {}}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserResponseDataSerializer(user)
            user.delete()
            return Response({'status': misc.HTTP_200_OK, 'data': serializer.data})
        else:
            return Response({'status': misc.HTTP_400_BAD_REQUEST, 'data': {}}, status=status.HTTP_400_BAD_REQUEST)


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
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user)
        result['data'] = serializer.data
        result['status'] = misc.HTTP_200_OK
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
            result['status'] = misc.HTTP_400_BAD_REQUEST

            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return RegisterView.create(self, request, *args, **kwargs)