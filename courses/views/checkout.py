from django.shortcuts import HttpResponse, render, redirect
from courses.models import Course, Video


def checkout(request,slug):
    course = Course.objects.get(slug=slug)    
    if not request.user.is_authenticated:
        return redirect("login")
    context = {"course":course}
    return render(request,template_name="courses/check_out.html",context=context)