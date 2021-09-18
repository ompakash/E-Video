from django.shortcuts import HttpResponse, render
from courses.models import Course


def home(request):
    courses = Course.objects.all()
    print(courses)
    return render(request,template_name="courses/home.html",context={"courses":courses})
