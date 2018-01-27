from .models import Document, Author, DocumentOfAuthor
from .serializer import DocumentSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .misc import HTTP_200_OK, HTTP_404_NOT_FOUND


class DocumentDetail(APIView):
    # TODO AUTHORIZATION
    @staticmethod
    def get(request, document_id):
        """
        GET request to get one particular document
        :param request:
        :param document_id:
        :return: JSON-Document and 200 if Document exists otherwise empty JSON and 404
        """
        try:
            data = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DocumentsByCriteria(APIView):
    # TODO AUTHORIZATION
    @staticmethod
    def get(request):
        """
        GET request to get set of document by criteria
        :param request:
        :return: JSON-Documents and 200 if Documents with such criteria exists
                 otherwise empty JSON and 404
        """
        author_name = request.GET.get('author_name', None)
        title = request.GET.get('title', None)
        year = request.GET.get('year', None)
        tag_ids = request.GET.get('tag_ids', None)
        size = request.GET.get('size', None)
        offset = request.GET.get('offset', None)

        data_query_set = Document.objects

        if author_name is not None:
            data_query_set = data_query_set.filter(documentofauthor__author__name__icontains=author_name)
        if title is not None:
            data_query_set = data_query_set.filter(title__icontains=title)
        if year is not None:
            data_query_set = data_query_set.filter(year=year)
        if tag_ids is not None:
            data_query_set = data_query_set.filter(tagofdocument__tag_id__in=tag_ids)
        if size is not None and offset is not None:
            data_query_set = data_query_set.filter()[int(offset):int(offset) + int(size)]

        serializer = DocumentSerializer(data_query_set, many=True)

        print(tag_ids, file=open('log.txt', 'w'))

        result = {'status': '', 'data': serializer.data}

        if serializer.data:
            result['status'] = HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)

        result['status'] = HTTP_404_NOT_FOUND
        return Response(result, status=status.HTTP_404_NOT_FOUND)
    
    
    
class Authorization(APIView):

    # GET http://127.0.0.1:8000/CORE/authorization/?email=test@inno.ru&password=8888

    @staticmethod
    def get(request):

        result = {'status': '', 'data': ''}

        try:
            # get information from request
            email = request.GET.get('email', None)
            password = request.GET.get('password', None)

            users = User.objects
            users = users.filter(email=email, password=password)

            if users.exists():                                                          # if exists all good
                result['status'] = status.HTTP_202_ACCEPTED
                return Response(result, status=status.HTTP_202_ACCEPTED)
            elif User.objects.filter(result, email=email).exists():
                result['status'] = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
                return Response(result, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)   # if exists but password incorrect

        except TypeError:
            pass

        result['status'] = status.HTTP_404_NOT_FOUND
        return Response(result, status=status.HTTP_404_NOT_FOUND)


class Registration(APIView):

    # POST http://127.0.0.1:8000/CORE/registration/?email=test@inno.ru&password=1234&role=1&first_name=PaVel&last_name=Nik&address=msk&phone=8800

    @staticmethod
    def post(request):

        result = {'status': '', 'data': ''}

        try:
            # get information from request
            email = request.GET.get('email', None)
            password = request.GET.get('password', None)
            role = request.GET.get('role', None)
            first_name = request.GET.get('first_name', None)
            last_name = request.GET.get('last_name', None)
            address = request.GET.get('address', None)
            phone = request.GET.get('phone', None)

            new_user = User(email=email,
                            password=password,
                            password_salt=password,
                            role=role,
                            first_name=first_name,
                            last_name=last_name,
                            address=address,
                            phone=phone)
            new_user.save()

            result['status'] = status.HTTP_201_CREATED
            return Response(result, status=status.HTTP_201_CREATED)

        except IntegrityError:

            result['status'] = status.HTTP_400_BAD_REQUEST
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        # TODO role can be not only allowed

