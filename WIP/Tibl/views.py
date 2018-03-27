from django.shortcuts import render

# Create your views here.

from .models import Course, Section, Post, Student, Teacher, Department, Message 

def index(request, pk):
    past_course_list = Section.objects.filter(students=pk)
    course_list = Section.objects.filter(students=pk).filter(season='Sp').filter(year=2018)
    have_messaged = [message.receiver for message in Message.objects.filter(sender=pk)] +\
                    [message.sender for message in Message.objects.filter(receiver=pk)]
    

    return render(
        request,
        'index.html',
        context={
        'past_course_list': past_course_list,
        'course_list': course_list,
        'have_messaged': have_messaged, 
        }
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
    class_num = num_

    course_  = Course.objects.get(number = num_)
    section = Section.objects.get(year = 2018, season = 'Sp')

    students_list = section.students.all()

    #print(students_list)

    return render(
        request,
        'classpage.html',
        #context={'name':course_name,'number':course_number,'year':year,'season':season, 'teachers':teachers, 'students':students},
        context={'classnum':course_.number, 'students':students_list}
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
