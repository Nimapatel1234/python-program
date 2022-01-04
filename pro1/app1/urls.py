from django.urls import path
from .views import hello,b,add

urlpatterns = [
    path('hello/',hello),
    path('b/',b),
    path('add/',add)
]