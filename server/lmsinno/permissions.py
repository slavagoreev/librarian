from rest_framework.views import exception_handler


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