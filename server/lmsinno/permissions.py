from rest_framework.response import Response
from rest_framework import status

from .models import User

from . import const


def permission_0(fn):
    def wrapper(request, *args, **kwargs):
        user = User.get_instance(request)
        print('wrapper 0')
        if user.role not in const.LIBRARIAN_ROLE_LIST:
            if 'role' in request.data and request.data['role'] != user.role:
                return Response(False, status=status.HTTP_403_FORBIDDEN)

            if 'user_id' in kwargs and int(kwargs['user_id']) != user.pk:
                return Response(False, status=status.HTTP_403_FORBIDDEN)
        else:
            if 'role' in request.data and request.data['role'] in const.LIBRARIAN_ROLE_LIST:
                return Response(False, status=status.HTTP_403_FORBIDDEN)
        return fn(request, *args, **kwargs)
    return wrapper


def permission_1(fn):
    def wrapper(request, *args, **kwargs):
        user = User.get_instance(request)
        print('wrapper 1')
        if user.role not in const.LIBRARIAN_ROLE_LIST:
            return Response(False, status=status.HTTP_403_FORBIDDEN)
        return fn(request, *args, **kwargs)
    return wrapper


def permission_2(fn):
    def wrapper(request, *args, **kwargs):
        user = User.get_instance(request)
        print('wrapper 2')
        if user.role not in [const.LIBRARIAN_BASE_ROLE,
                             const.LIBRARIAN2_ROLE,
                             const.LIBRARIAN3_ROLE]:
            return Response(False, status=status.HTTP_403_FORBIDDEN)
        return fn(request, *args, **kwargs)
    return wrapper


def permission_3(fn):
    def wrapper(request, *args, **kwargs):
        user = User.get_instance(request)
        print('wrapper 3')
        if user.role not in [const.LIBRARIAN_BASE_ROLE,
                             const.LIBRARIAN3_ROLE]:
            return Response(False, status=status.HTTP_403_FORBIDDEN)
        return fn(request, *args, **kwargs)
    return wrapper



