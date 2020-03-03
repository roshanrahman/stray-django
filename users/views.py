from django.shortcuts import render
from users.responses import AbstractResponse
# Create your views here.


def register(request):
    return AbstractResponse().json()
