from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status


#@api_view(['GET', 'POST'])
#def student_list(request):
  # '''
 #   List all code snippets, or create a new snippet.
   # '''
 #   if request.method == 'GET':
  #      snippets = Student.objects.all()
   #     serializer = StudentSerializer(snippets, many=True)
    #    return Response(serializer.data)

    #elif request.method == 'POST':
     #   serializer = StudentSerializer(data=request.data)
      #  if serializer.is_valid():
       #     serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#@api_view(['GET', 'PUT', 'DELETE'])
#def student_detail(request, pk=None):
  #  """
 #   Retrieve, update or delete a code snippet.
 #   """
 #   try:
  #      snippet = Student.objects.get(pk=pk)
   # except Student.DoesNotExist:
    #    return Response(status=status.HTTP_404_NOT_FOUND)

    #if request.method == 'GET':
     #   serializer = StudentSerializer(snippet)
      #  return Response(serializer.data)

    #elif request.method == 'PUT':
     #   serializer = StudentSerializer(snippet, data=request.data)
      #  if serializer.is_valid():
       #     serializer.save()
        #    return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   # elif request.method == 'DELETE':
    #    snippet.delete()
     #   return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_list(request,pk=None):
	if request.method=='GET':
		id=pk	
		if id is not None:
			stu=Student.objects.get(id=id)
			serializer=StudentSerializer(stu)
			return Response(serializer.data)

		stu=Student.objects.all()
		serializer= StudentSerializer(stu,many=True)
		    #serializer=StudentSerializer(stu,many=True)
		return Response(serializer.data)
		    #return Response(serializer.data)
	      
	if request.method=='POST':
		serializer=StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		    
	if request.method=='PUT':
		#id=request.data.get('id')
		stu=Student.objects.get(pk=pk)
		serializer=StudentSerializer(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


	if request.method=='PATCH':
		#id=request.data.get('id')
		stu=Student.objects.get(pk=pk)
		serializer=StudentSerializer(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	if request.method=='DELETE':
		#id=request.data.get('id')
		stu=Student.objects.get(pk=pk)
		stu.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



