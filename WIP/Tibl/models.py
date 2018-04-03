from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
	department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200, null=True)
	number = models.CharField(max_length=10)

class Section(models.Model):
	year = models.IntegerField()
	season_enum = (
		('F', 'Fall'),
		('Sp', 'Spring'),
		('W', 'Winter'),
		('Su', 'Summer'),
	)
	season = models.CharField(max_length=2, choices=season_enum, null=True)
	teachers = models.ManyToManyField('Teacher')
	students = models.ManyToManyField('Student')
	course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

class Post(models.Model):
	poster = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
	content = models.TextField(max_length=10000)
	creation_date = models.DateTimeField(auto_now_add=True)
	section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)


class Student(models.Model):
	"""
	Model representing a student
	"""
	full_name = models.CharField(max_length=60)
	grad_year = models.IntegerField()
	profile_picture = models.ImageField(upload_to="profile_pictures")
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

	
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.full_name
	
class Teacher(models.Model):
	"""
	Model representing a Teacher
	"""
	full_name = models.CharField(max_length=60)
	department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
	profile_picture = models.ImageField(upload_to="profile_pictures")

	
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.full_name

class Department(models.Model):
	"""
	Model representing a Department
	"""
	name = models.CharField(max_length=60)
	abbreviation = models.CharField(max_length=10)
	
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.name

class Message(models.Model):
	"""
	Model representing a private message between two users
	"""
	sender = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, related_name = 'sender') 
	receiver = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, related_name = 'receiver')
	content = models.TextField(max_length=1000)
	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""
		String for representing the Model object
		"""
		return self.content

