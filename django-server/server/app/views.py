from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    models.do_smth()

    hello = models.hello()
    return HttpResponse(hello)