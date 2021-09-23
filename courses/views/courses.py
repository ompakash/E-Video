from django.shortcuts import HttpResponse, render
from courses.models import Course, Video


def coursePage(request,slug):
    course = Course.objects.get(slug=slug)
    serial_no = request.GET.get('lecture')
    videos = course.video_set.all ().order_by("serial_no")
    if serial_no is None:
        serial_no = 1
    video = Video.objects.get(serial_no = serial_no, course = course)
    
    context = {"course":course,
        "video":video,
        "videos":videos}
    return render(request,template_name="courses/course_page.html",context=context)