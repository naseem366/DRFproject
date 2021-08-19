from django.shortcuts import render
#from rest_framework.response import Response
#from rest_framework import status
#from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import (ListAPIView,CreateAPIView,
RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,
RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)

class StudentList(ListAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentCreate(CreateAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentRetrieve(RetrieveAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentUpdate(UpdateAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentDestroy(DestroyAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentListCreate(ListCreateAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	lookup_field = 'pk'




'''
class StudentAPI(APIView):
	def get(self,request,pk=None,format=None):
		id=pk	
		if id is not None:
			stu=Student.objects.get(id=id)
			serializer=StudentSerializer(stu)
			return Response(serializer.data)

		stu=Student.objects.all()
		serializer= StudentSerializer(stu,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer=StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self,request,pk,format=None):
		stu=Student.objects.get(pk=pk)
		serializer=StudentSerializer(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


	def delete(self,request,pk,format=None):
		stu=Student.objects.get(pk=pk)
		stu.delete()
		return Response({'msg':'data deleted'},status=status.HTTP_204_NO_CONTENT)



	def patch(self,request,pk,format=None):

	    stu=Student.objects.get(pk=pk)
	    serializer=StudentSerializer(stu,data=request.data,partial=True)
	    if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


'''