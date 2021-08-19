from django.shortcuts import render
#from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
#from rest_framework import status
#from rest_framework.views import APIView
from rest_framework import viewsets
# Create your views here.
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly


class StudentModelViewSet(viewsets.ModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	#authentication_classes=[BasicAuthentication]
	authentication_classes=[SessionAuthentication]
	#permission_classes=[IsAuthenticated]
	permission_classes=[IsAuthenticatedOrReadOnly]
	#permission_classes=[AllowAny]
	#permission_classes=[IsAdminUser]

