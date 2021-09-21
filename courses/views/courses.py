from django.shortcuts import HttpResponse, render
from courses.models import Course


def coursePage(request,slug):
    course = Course.objects.get(slug=slug)
    context = {"course":course}
    return render(request,template_name="courses/course_page.html",context=context)