from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin


#no required pk so
class StudentList(GenericAPIView,ListModelMixin,CreateModelMixin):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

#required pk so 

class StudentRetrieve(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	def get(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)





'''
class StudentList(GenericAPIView,ListModelMixin):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)


class StudentCreate(GenericAPIView,CreateModelMixin):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)


class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	def get(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)


class StudentUpdate(GenericAPIView,UpdateModelMixin):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)


class StudentDestroy(GenericAPIView,DestroyModelMixin):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)




from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework.views import APIView

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