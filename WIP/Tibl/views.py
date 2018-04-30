import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.forms import ModelForm
from .models import Course, Section, Post, Student, Teacher, Department, Message, User
from .forms import StudentForm, AddSearchedClassForm


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, prefix='user')
        student_form = StudentForm(request.POST, request.FILES, prefix='student')
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            userprofile = student_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return redirect('index')
    else:
        user_form = UserCreationForm(prefix='user')
        student_form = StudentForm(prefix='student')
    return render(request, 
                    'register.html', 
                    dict(userform=user_form,
                         studentform=student_form))

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
        context={'students':students_list, 
                 'year':year, 
                 'season':season, 
                 'teachers':teachers_list, 
                 'name':course_name, 
                 'department':course_department, 
                 'number':course_number }
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

@login_required
def class_search(request):
    if request.method == 'POST':
        # If statement to handle the search
        if 'class_search' in request.POST.keys():
            search_term = request.POST['class_search']
            terms = search_term.split(' ')

            # matching_classes is like {'str_rep_of_class': number_of_hits}
            # str_class_dict is like {'str_rep_of_class': Section_object}
            matching_classes = {}
            str_class_dict = {}

            # Consider each word in the search separately
            for term in terms:
                cur_match = Section.objects.filter(Q(course__number=term) | \
                                                   Q(course__name__icontains=term) | \
                                                   Q(course__department__name__icontains=term) | \
                                                   Q(course__department__abbreviation__icontains=term)).distinct()

                # Remove classes the user is in
                cur_match = cur_match.filter(~Q(students=request.user.student.pk))

                cur_match = list(cur_match)
                for match in cur_match:
                    match_str = match.__str__
                    if match_str in matching_classes.keys():
                        matching_classes[match_str] = matching_classes[match_str] + 1
                    else:
                        matching_classes[match_str] = 1
                        str_class_dict[match_str] = match

            match_list = sorted(matching_classes.items(), key=lambda x: x[1])
            match_obj_list = []
            for pair in match_list:
                match_obj_list.append(str_class_dict[pair[0]])

            match_obj_list = list(reversed(match_obj_list))
            added_class_form = AddSearchedClassForm(choices=[(obj.pk, obj.to_string()) for obj in match_obj_list])
            return render(request, 
                          'class_search.html',
                          context={'add_class_form':added_class_form})

        # If statement to handle adding classes
        elif 'sections' in request.POST.keys():
            for section in request.POST['sections']:
                Section.objects.get(pk=section).students.add(request.user.student)

    return render(request, 'class_search.html')




def friendprofile(request, profile_id):
    student = Student.objects.get(id = profile_id)
    sections = Section.objects.filter(students__id__exact=profile_id)

    return render(
        request,
        'friendprofile.html',
        context={'student':student, 'sections':sections}
    )


from django.http import HttpResponseRedirect
from django.urls import reverse

def register_section_current(request, num_):
    """
    View function for registering for a current class
    """
    course = Course.objects.get(number__exact = num_)
    section = Section.objects.get(course__id__exact=course.id, year__exact=2018)
    student = Student.objects.get(user__id__exact=request.user.id)

   # Create a form instance and populate it with data from the request (binding):
    if student not in section.students.all():
        section.students.add(student)
        section.save()

    return HttpResponseRedirect(reverse('index'))
