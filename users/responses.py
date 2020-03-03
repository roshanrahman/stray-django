from django.http import JsonResponse

ERRORS = {
    'USER_ALREADY_EXISTS': 'An account already exists with the phone number you provided',
    'INVALID PASSWORD': 'The password you provided is invalid',
    'INVALID_PHONE_NUMBER': 'The phone number you provided is of an incorrect format'
}


def resolve_errors_to_dict(error_code):
    if error_code is None:
        return None
    if ERRORS.get(error_code, None) is not None:
        return {
            'error_code': error_code,
            'error_message': ERRORS.get(error_code)
        }
    raise KeyError('This is not a valid error code')


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
