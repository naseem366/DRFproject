from django.shortcuts import render
#from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
#from rest_framework import status
#from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

'''
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

'''
