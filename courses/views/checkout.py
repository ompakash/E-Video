from django.shortcuts import HttpResponse, render, redirect
from courses.models import Course, Video


def checkout(request,slug):
    course = Course.objects.get(slug=slug)    
    if not request.user.is_authenticated:
        return redirect("login")

    action = request.GET.get('action')
    order = None
    if action == 'create_payment':
        print("Creating Order Object")
        order = "Order Created"


    context = {"course":course,"order":order}
    return render(request,template_name="courses/check_out.html",context=context)