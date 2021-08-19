from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField()
	phone=models.IntegerField()
	city=models.CharField(max_length=200)
	state=models.CharField(max_length=200)
	country=models.CharField(max_length=200)
