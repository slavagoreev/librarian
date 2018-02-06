import re

from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import exception_handler

from lmsinno.models import User


class DocumentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        try:

            user = User.get_instance(request)

            if request.method == 'GET':
                result = True
            elif request.method == 'POST' and user.role == 2:
                result = True
            elif request.method == 'DELETE' and user.role == 2:
                result = True
            elif request.method == 'PATCH' and user.role == 2:
                result = True
            else:
                result = False

            return result
        except Token.DoesNotExist:
            return False
        except KeyError:
            return False


class OrderPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        try:

            user = User.get_instance(request)

            if request.method == 'GET' and user.role == 2:
                result = True
            elif request.method == 'POST' and user.role == 2:
                result = True
            elif request.method == 'DELETE' and user.role == 2:
                result = True
            elif request.method == 'PATCH' and user.role == 2:
                result = True
            else:
                result = False

            return result
        except Token.DoesNotExist:
            return False
        except KeyError:
            return False


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    data = {'status': '',
            'data': {}}

    # Now add the HTTP status code to the response.

    if response is not None:
        if response.status_code == 401:
            data['status'] = 'HTTP_401_UNAUTHORIZED'
        elif response.status_code == 403:
            data['status'] = 'HTTP_403_FORBIDDEN'
        response.data = data

    return response