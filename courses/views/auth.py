from django.shortcuts import HttpResponse, render
from courses.models import Course, Video

def signup(request):
    return render(request,template_name="courses/signup.html")


def login(request):
    return render(request,template_name="courses/login.html")