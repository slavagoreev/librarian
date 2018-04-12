from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import permissions

from .models import User

from . import const


class LibrarianPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = User.get_instance(request)

        if not user:
            return False

        if request.method == 'GET' and user.role == (const.LIBRARIAN_BASE_ROLE or
                                                     const.LIBRARIAN1_ROLE or
                                                     const.LIBRARIAN2_ROLE or
                                                     const.LIBRARIAN3_ROLE):
            result = True

        elif request.method == 'PATCH' and user.role == (const.LIBRARIAN_BASE_ROLE or
                                                         const.LIBRARIAN1_ROLE or
                                                         const.LIBRARIAN2_ROLE or
                                                         const.LIBRARIAN3_ROLE):

            result = True

        elif request.method == 'POST' and user.role == (const.LIBRARIAN_BASE_ROLE or
                                                        const.LIBRARIAN2_ROLE or
                                                        const.LIBRARIAN3_ROLE):
            result = True

        elif request.method == 'DELETE' and user.role == (const.LIBRARIAN_BASE_ROLE or
                                                          const.LIBRARIAN3_ROLE):
            result = True

        else:

            result = False

        return result


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = User.get_instance(request)

        flag = user.pk == int(request.META['PATH_INFO'].split('/')[-1])

        if not user:
            return False

        if request.method == 'GET' and (flag or user.role == const.LIBRARIAN_BASE_ROLE):
            result = True
        elif request.method == 'POST' and (flag or user.role == const.LIBRARIAN_BASE_ROLE):
            result = True
        elif request.method == 'DELETE' and user.role == const.LIBRARIAN_BASE_ROLE:
            result = True
        elif request.method == 'PATCH':
            if user.role == const.LIBRARIAN_BASE_ROLE:
                result = True
            elif flag:
                result = True
                try:
                    request.data['role']
                    result = False
                except MultiValueDictKeyError:
                    pass
            else:
                result = False
        else:
            result = False

        return result
