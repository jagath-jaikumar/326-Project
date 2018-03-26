from django.shortcuts import render

# Create your views here.

from .models import Course, Section, Post, Student, Teacher, Department

def index(request, pk):
    past_course_list = Section.objects.filter(student=pk).course.name
    course_list = Section.objects.filter(student=pk).filter(season='Sp').filter(year=2018).course.name
    have_messaged = Message.objects.filter(sender=pk).receiver | Message.objects.filter(receiver=pk).sender

    return render(
        request,
        'index.html',
        context={
        'past_course_list': pastcourse_list,
        'course_list': course_list,
        'have_messaged': have_messaged, 
        }
    )


def classpage(request):
    course_name = Section.course.name
    course_number = Section.course.number
    year = Section.year
    season = Section.season
    teachers = Section.teachers
    students = Section.students

    return render(
        request,
        'classpage.html',
        context={'name':course_name,'number':course_number,'year':year,'season':season, 'teachers':teachers, 'students':students},
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

def home(request):
    return render(
        request,
        'home.html'
    )



















