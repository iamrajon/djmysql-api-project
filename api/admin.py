from django.contrib import admin
from api.models import Courses, Student

# Register your models here.

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'title', 'description', 'duration', 'fees']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stu_id', 'name', 'roll', 'gender', 'city', 'phone', 'date_enrolled', 'courses']
