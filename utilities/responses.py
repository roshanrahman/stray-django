from django.http import JsonResponse
from utilities.errors import INVALID_ROUTE, USER_DOES_NOT_EXIST
from users.models import CustomUser
from utilities.jwt import encode_jwt, decode_jwt


def resolve_errors_to_dict(error_obj=None):

    if error_obj is None:
        return None
    return {
        'code': error_obj[0],
        'message': error_obj[1]
    }


class StandardResponse(JsonResponse):

    error = None
    data = None

    def __init__(self, error_code=None, data=None):
        self.error = resolve_errors_to_dict(error_code)
        self.data = data

    def json(self):
        return JsonResponse({
            'data': self.data,
            'error': self.error,
        })


class ReportResponse(StandardResponse):

    def __init__(self, report_list):
        list_of_reports = report_list
        if list_of_reports is None:
            super().__init__(error_code=INVALID_ROUTE)
        else:
            json_list = []
            for report in list_of_reports:
                json_object = dict()
                json_object['citizen_id'] = report.citizen.id
                json_object['images'] = report.images
                json_object['multiple'] = report.multiple
                json_object['latitude'] = report.latitude
                json_object['longitude'] = report.longitude
                json_object['status'] = report.status
                json_list.append(json_object)
            data = {
                'count': len(json_list),
                'values': json_list
            }
            super().__init__(data=data)


class UserResponse(StandardResponse):
    def __init__(self, user_id):
        user = None
        try:
            user = CustomUser.objects.get(pk=int(user_id))
            user_json = dict()
            user_json['jwt'] = str(encode_jwt(user.id), 'utf-8')
            user_json['phone'] = user.phone
            user_json['account_type'] = user.account_type
            super().__init__(data=user_json)
        except Exception as e:
            print(e)
            super().__init__(error_code=USER_DOES_NOT_EXIST)
