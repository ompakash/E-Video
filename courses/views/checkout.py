from django.shortcuts import HttpResponse, render, redirect
from courses.models import Course, Video
from code_om.settings import *
from datetime import datetime
from time import time

import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))


def checkout(request,slug):
    course = Course.objects.get(slug=slug)    
    user = None
    if not request.user.is_authenticated:
        return redirect("login")

    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    if action == 'create_payment':
        amount = int((course.price - (course.price * course.discount * 0.01))*100)
        currency = "INR"
        notes ={
            'email':user.email,
            'name': f'{user.first_name}{user.last_name}',
        }
        receipt = f"codeom-{int(time())}"
        client.order.create({'receipt':receipt,
        'notes':notes,
        'amount':amount,
        'currency':currency})


    context = {"course":course,"order":order}
    return render(request,template_name="courses/check_out.html",context=context)

    