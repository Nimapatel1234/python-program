from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(self):
    return HttpResponse("hello world")
def b(self):
    return HttpResponse("bye")
def add(self):
    a=23
    b=43
    c=a+b
    return HttpResponse(c)