from django.db import models

# Create your models here.

class Course(models.Model):
	department = models.CharField(max_length=200)
	number = models.CharField(max_length=10)

class Section(models.Model):
	year = models.IntegerField()
	season = (
		('F', 'Fall'),
		('Su', 'Spring'),
		('W', 'Winter'),
		('Su', 'Summer'),
	)
	teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
	student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
	post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

class Post(models.Model):
	poster = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
	course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
	content = models.TextField(max_length=10000)
	creation_date = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
	"""
	Model representing a student
	"""
	full_name = models.CharField(max_length=60)
	grad_year = models.IntegerField()
	profile_picture = models.ImageField(upload_to="profile_pictures")

	
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

