from django.shortcuts import render

# Create your views here.

from .models import Course, Section, Post, Student, Teacher, Department

def index(request):
    return render(
        request,
        'index.html',
    )

def classpage(request, num_):

    section = Section.objects.get(id=num_)
    year = section.year
    season = section.season
    teachers_list = section.teachers.all()
    course = section.course
    course_name = course.name
    course_number = course.number
    course_department = course.department
    students_list = section.students.all()

    return render(
        request,
        'classpage.html',
        context={'students':students_list, 'year':year, 'season':season, 'teachers':teachers_list, 'name':course_name, 'department':course_department, 'number':course_number }
    )

def messaging(request):
    return render(
        request,
        'messaging.html',
    )

def myprofile(request):
    return render(
        request,
        'myprofile.html',
    )

def friendprofile(request):
    return render(
        request,
        'friendprofile.html',
    )