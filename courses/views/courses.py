from django.shortcuts import HttpResponse, render
from courses.models import Course


def coursePage(request,slug):
    context = {"slug":slug}
    return render(request,template_name="courses/course_page.html",context=context)