from django.contrib import admin
from django.urls import path
from courses.views import home

urlpatterns = [
    path('', home , name = "home")
]

