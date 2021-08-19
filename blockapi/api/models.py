from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField()
	phone=models.IntegerField()
	city=models.CharField(max_length=200)
	state=models.CharField(max_length=200)
	country=models.CharField(max_length=200)

class StudentUser(models.Model):
	class Meta:
		model=User
		fields=['username','email','password1','password2']

    


