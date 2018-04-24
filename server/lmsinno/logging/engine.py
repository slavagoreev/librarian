from .logging_serializer import LogRecordSerializer
from ..models import User

import json

HTTP_METHOD_MAPPING = {'GET': 0,
                       'PUT': 1,
                       'DELETE': 2,
                       'POST': 3,
                       'UPDATE': 4,
                       'PATCH': 5,
                       'CREATE': 6}

STATUS_CODE_MAPPING = {'200': 0,
                       '202': 0,
                       '404': 2,
                       '400': 2}


def make_log_record(user, log_msg_type, method_type, params, response_status,  description):
    data = {'user': user,
            'log_msg_type': log_msg_type,
            'method_type': method_type,
            'description': description,
            'params': json.dumps(params),
            'response_status': response_status}

    serializer = LogRecordSerializer(data=data)

    if serializer.is_valid():
        serializer.save()


def logging(description):
    def decorator(http_method):
        def wrapper(request, *args, **kwargs):

            response = http_method(request, *args, **kwargs)

            log_record = {'user': User.get_instance(request).id,
                          'log_msg_type': STATUS_CODE_MAPPING[response.status_code],
                          'method_type': HTTP_METHOD_MAPPING[request.method],
                          'params': {'get_params': args[0],
                                     'body_params': request.query_params},
                          'response_status': response.status_code,
                          'description': description}

            make_log_record(**log_record)

            return response
        return wrapper
