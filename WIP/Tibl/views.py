from django.shortcuts import render

# Create your views here.

from .models import Course, Section, Post, Student, Teacher, Department

def index(request):
    return render(
        request,
        'index.html',
    )

def classpage(request, num_):
    '''
    course_name = Section.course.name
    course_number = Section.course.number
    year = Section.year
    season = Section.season
    teachers = Section.teachers
    students = Section.students
    '''

    section = Section.objects.get(id=num_)
    
    students_list = section.students.all()

    #print(students_list)

    return render(
        request,
        'classpage.html',
        #context={'name':course_name,'number':course_number,'year':year,'season':season, 'teachers':teachers, 'students':students},
        context={'students':students_list}
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