from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Response from django")


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About page")


def welcome(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('response.html')
    return HttpResponse(template.render())
