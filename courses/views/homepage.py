from django.shortcuts import HttpResponse, render



def home(request):
    return HttpResponse("Home Page")
