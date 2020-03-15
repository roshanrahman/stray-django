from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.views.decorators.http import require_POST
from utilities.responses import StandardResponse, UserResponse
from utilities.errors import USER_DOES_NOT_EXIST, INVALID_ROUTE, INVALID_PARAMS, USER_ALREADY_EXISTS, INVALID_PASSWORD
from users.models import CustomUser
# Create your views here.


@require_POST
def register(request):
    phone = request.POST.get('phone')
    account_type = request.POST.get('account_type', 'citizen')
    password = request.POST.get('password')
    if not phone or not password:
        return StandardResponse(error_code=INVALID_PARAMS).json()
    try:
        user = CustomUser(
            phone=phone,
            account_type=account_type
        )
        user.set_password(password)
        user.save()
        return UserResponse(user.id).json()
    except IntegrityError as e:
        print(e)
        return StandardResponse(error_code=USER_ALREADY_EXISTS).json()
    return StandardResponse(error_code=INVALID_PARAMS).json()


@require_POST
def login(request):
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    if not phone or not password:
        return StandardResponse(error_code=INVALID_PARAMS).json()
    try:
        user = CustomUser.objects.get(phone=phone)
    except:
        return StandardResponse(error_code=USER_DOES_NOT_EXIST).json()
    user = authenticate(phone=phone, password=password)
    if user is not None:
        return UserResponse(user.id).json()
    return StandardResponse(error_code=INVALID_PASSWORD).json()


def page_not_found(request, exception):
    return StandardResponse(error_code=INVALID_ROUTE).json()
