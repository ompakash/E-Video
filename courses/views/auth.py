from django.shortcuts import HttpResponse, render
from courses.models import Course, Video
from django.contrib.auth.forms import UserCreationForm
from courses.forms import RegistrationForm

def signup(request):
    if(request.method == "GET"):
        form = RegistrationForm()
        return render(request,template_name="courses/signup.html",context = { 'form' : form } )
    
    else:
        return HttpResponse("POST REQUEST")


def login(request):
    return render(request,template_name="courses/login.html")