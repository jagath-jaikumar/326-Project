from django.shortcuts import render

# Create your views here.

from .models import Course, Section, Post, Student, Teacher, Department

def index(request):
    return render(
        request,
        'index.html',
    )

def classpage(request):
    return render(
        request,
        'classpage.html',
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