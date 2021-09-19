from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from code_om.settings import MEDIA_ROOT, MEDIA_URL 
from courses.views import home

urlpatterns = [
    path('', home , name = "home")
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)

