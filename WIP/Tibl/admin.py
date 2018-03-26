from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, Course, Section, Post, Department, Message

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Post)
admin.site.register(Department)
admin.site.register(Message)