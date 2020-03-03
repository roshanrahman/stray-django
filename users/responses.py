from django.http import JsonResponse

ERRORS = {
    'USER_ALREADY_EXISTS': 'An account already exists with the phone number you provided',
    'INVALID PASSWORD': 'The password you provided is invalid',
    'INVALID_PHONE_NUMBER': 'The phone number you provided is of an incorrect format'
}


def resolve_errors_to_dict(error_obj=None):
    if error_obj is None:
        return None
    return {
        'code': error_obj[0],
        'message': error_obj[1]
    }


class AbstractResponse(JsonResponse):
    error = None
    data = None

    def __init__(self, *args, **kwargs):
        self.error = resolve_errors_to_dict(kwargs.get('error_code', None))
        self.data = kwargs.get('data', None)

    def json(self):
        return JsonResponse({
            'data': self.data,
            'error': self.error,
        })
