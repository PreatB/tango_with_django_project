from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Rango says hey there partner! <a href='rango/about'> Link</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/'> Link </a>")