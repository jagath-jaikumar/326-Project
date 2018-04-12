from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import operator
from .models import Course, Section, Post, Student, Teacher, Department, Message, User 
import datetime


@login_required
def index(request):
    poster = Student.objects.get(user=request.user.pk)
    student_pk = poster.pk
    if request.method == 'POST':
        course_number = request.POST['class_name'].split(' ')[-1]
        course_department = ' '.join(request.POST['class_name'].split(' ')[0:-1])
        post_section = Section.objects.get(course__department__name=course_department, course__number=course_number, 
                                           season='Sp', year=2018)
        cur_post = Post(content=request.POST["post_text"], creation_date=datetime.datetime, 
                        poster=poster, section=post_section)
        cur_post.save()

    past_section_list = Section.objects.filter(students=student_pk).filter(~(Q(year=2018) & Q(season='Sp')))
    section_list = Section.objects.filter(students=student_pk).filter(season='Sp').filter(year=2018)
    have_messaged = [message.receiver for message in Message.objects.filter(sender=student_pk)] +\
                    [message.sender for message in Message.objects.filter(receiver=student_pk)]

    other_classmates = Student.objects.filter(section__in=section_list).filter(~Q(pk=student_pk)).distinct()

    # remove non-distinct elements
    have_messaged = list(set(have_messaged))

    posts = Post.objects.filter(section__in=section_list)
    ordered = posts.order_by('-creation_date')

    return render(
        request,
        'index.html',
        context={
        'past_section_list': past_section_list,
        'section_list': section_list,
        'have_messaged': have_messaged,
        'cur_user': student_pk,
        'posts': ordered, 
        'other_classmates': other_classmates,
        }
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

@login_required
def messaging(request):
    cur_user = request.user.pk
    cur_student = Student.objects.get(user=cur_user)
    messages = Message.objects.filter(Q(sender=cur_student) | Q(receiver=cur_student))
    return render(
        request,
        'messaging.html',
        context={'messages':messages}
    )

@login_required
def myprofile(request):
    profile_id = Student.objects.get(user=request.user.pk).pk
    student = Student.objects.get(id = profile_id)
    sections = Section.objects.filter(students__id__exact=profile_id)

    return render(
        request,
        'myprofile.html',
        context={'student':student, 'sections':sections}
    )

def friendprofile(request, profiled_id):
    student = Student.objects.get(id = profile_id)
    sections = Section.objects.filter(students__id__exact=profile_id)

    return render(
        request,
        'friendprofile.html',
        context={'student':student, 'sections':sections}
    )
