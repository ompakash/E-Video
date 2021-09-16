from django.contrib import admin
from courses.models import Course,Tag,Prerequisite,Learning


class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite
        
class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,LearningAdmin,PrerequisiteAdmin]

# Register your models here.
admin.site.register(Course,CourseAdmin)
