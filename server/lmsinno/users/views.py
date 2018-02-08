import datetime

from ..permissions import AuthenticatedUserPermission
from ..models import User
from .serializer import UserSerializer, UserSafeSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import detail_route

from ..misc import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, \
    HTTP_409_CONFLICT, HTTP_401_UNAUTHORIZED

import re
import base64


#
# class UsersView(APIView):
#     @detail_route(methods=['get'], permission_classes=[AuthenticatedUserPermission])
#     def get(self, request):
#         """
#         GET custom user
#         """
#         result = {'status': '', 'data': {}}
#
#         try:
#             user = result
#         except Document.DoesNotExist:
#             result['status'] = HTTP_404_NOT_FOUND
#             return Response(result, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = UserSafeSerializer(user)
#         result['status'] = HTTP_200_OK
#         result['data'] = serializer.data
#
#         return Response(result, status=status.HTTP_200_OK)
#
#     @detail_route(methods=['post'], permission_classes=[AllowAny], url_path='signin')
#     def signin(self, request):
#         """
#         GET request for Signing Up
#         :param request:
#         :return: HTTP_202_ACCEPTED: Sign In is successful
#                  HTTP_401_UNAUTHORIZED: Wrong username or password
#                  HTTP_400_BAD_REQUEST: Wrong format of input data
#         """
#         result = {'status': '', 'data': {}}
#
#         if 'HTTP_AUTHORIZATION' in request.META:
#             auth = request.META['HTTP_AUTHORIZATION'].split()
#             if len(auth) == 2:
#                 if auth[0].lower() == "basic":
#                     username, password = base64.b64decode(auth[1]).decode('utf-8').split(':')
#                     user = User.objects.filter(username=username, password=password)
#                     if user.exists():
#                         token = Token.objects.get(user=user.get())
#                         result['status'] = HTTP_202_ACCEPTED
#                         result['data']['token'] = token.key
#                         result['data']['user'] = user
#                         return Response(result, status=status.HTTP_202_ACCEPTED)
#                     else:
#                         result['status'] = HTTP_401_UNAUTHORIZED
#                         return Response(result, status=status.HTTP_401_UNAUTHORIZED)
#
#         result['status'] = HTTP_400_BAD_REQUEST
#         return Response(result, status=status.HTTP_400_BAD_REQUEST)
#
#     @detail_route(methods=['post'], permission_classes=[AllowAny], url_path='signup')
#     def signup(self, request):
#         """
#         POST request for Signing Up
#         :param request:
#         :return: HTTP_202_ACCEPTED and JSON: Sign Up is successful
#                  HTTP_400_BAD_REQUEST and JSON: Wrong format of input data
#         """
#         result = {'status': '', 'data': {}}
#
#         serializer = UserSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#
#             result['status'] = HTTP_202_ACCEPTED
#             result['data'] = {'token': Token.objects.get(user=serializer.instance).key,
#                               'user': serializer.data}
#
#             return Response(result, status=status.HTTP_202_ACCEPTED)
#
#         result['status'] = HTTP_400_BAD_REQUEST
#         result['data'] = serializer.errors
#
#         return Response(result, status=status.HTTP_400_BAD_REQUEST)
#
