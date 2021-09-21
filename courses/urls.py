from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from code_om.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL,STATIC_ROOT
from courses.views import home,coursePage


urlpatterns = [
    path('', home , name = "home"),
    path('course/<str:slug>', coursePage , name = "coursepage"),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)