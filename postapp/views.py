from django.shortcuts import render
from django.http import HttpResponse


def indexView(request):
    return HttpResponse("Hello world !")
