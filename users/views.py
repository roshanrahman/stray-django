from django.shortcuts import render
from users.responses import AbstractResponse
from utilities.errors import USER_DOES_NOT_EXIST
# Create your views here.


def register(request):
    return AbstractResponse(error_code=USER_DOES_NOT_EXIST).json()
