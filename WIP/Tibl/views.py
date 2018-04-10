from django.shortcuts import render
from django.db.models import Q
from .models import Course, Section, Post, Student, Teacher, Department, Message 

def index(request, pk):
    past_section_list = Section.objects.filter(students=pk).filter(~(Q(year=2018) & Q(season='Sp')))
    section_list = Section.objects.filter(students=pk).filter(season='Sp').filter(year=2018)
    have_messaged = [message.receiver for message in Message.objects.filter(sender=pk)] +\
                    [message.sender for message in Message.objects.filter(receiver=pk)]

    other_classmates = Student.objects.filter(section__in=section_list).filter(~Q(pk=pk)).distinct()

    # remove non-distinct elements
    have_messaged = list(set(have_messaged))

    posts = Post.objects.filter(id__in=section_list)

    return render(
        request,
        'index.html',
        context={
        'past_section_list': past_section_list,
        'section_list': section_list,
        'have_messaged': have_messaged,
        'cur_user': pk,
        'posts': posts, 
        'other_classmates': other_classmates,
        }
    )

def default_index(request):
    return index(request, pk=1)

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

def messaging(request, profile_id):
    messages = Message.objects.all()
    return render(
        request,
        'messaging.html',
        context={'messages':messages}
    )

def myprofile(request, profile_id):

    student = Student.objects.get(id = profile_id)
    sections = Section.objects.filter(students__id__exact=profile_id)

    return render(
        request,
        'myprofile.html',
        context={'student':student, 'sections':sections}
    )

def friendprofile(request, profile_id):
    student = Student.objects.get(id = profile_id)
    sections = Section.objects.filter(students__id__exact=profile_id)

    return render(
        request,
        'friendprofile.html',
        context={'student':student, 'sections':sections}
    )

def register_section_current(request, section_pk):
    """
    View function for registering for a current class
    """
    section = Section.objects.get(id=section_pk)
    student = Student.objects.filter(user__id__exact=request.user.id)

   # Create a form instance and populate it with data from the request (binding):
    if student not in section.students:
        section.students.append(student)
        section.save()

    return HttpResponseRedirect(reverse('index'))