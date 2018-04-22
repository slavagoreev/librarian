from .logging_serializer import LogRecordSerializer

import json


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
    else:
        print(serializer.errors)
