from django.shortcuts import render
from utilities.responses import StandardResponse
from utilities.errors import USER_DOES_NOT_EXIST, INVALID_ROUTE
# Create your views here.


def register(request):
    return StandardResponse(error_code=USER_DOES_NOT_EXIST).json()


def page_not_found(request, exception):
    return StandardResponse(error_code=INVALID_ROUTE).json()
