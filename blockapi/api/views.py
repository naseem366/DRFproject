from django.shortcuts import render
#from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
#from rest_framework import status
#from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.status import (
                                        HTTP_200_OK,
                                    	HTTP_400_BAD_REQUEST,
                                    	HTTP_204_NO_CONTENT,
                                    	HTTP_201_CREATED,
                                    	HTTP_500_INTERNAL_SERVER_ERROR,
                                        HTTP_404_NOT_FOUND,
 
                                   ) 
from .serializers import *
from .models import *

class BlockUserAPIView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)

        stu=Student.objects.all()
        serializer= StudentSerializer(stu,many=True)
        return Response(serializer.data)


    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request,*args,**kwargs):
        user_id = self.kwargs['pk']
        try:
            user=User.objects.get(id=user_id)
        except:
            return Response({
                'success':'False',
                'message':'No user to block'
                },status=HTTP_400_BAD_REQUEST)

        if user.is_active == True:
            user.is_active = False
            user.save()
            return Response({
                        'success':'True',
                        'message':'User blocked successfully'
                        },status=HTTP_200_OK)
        else:
            return Response({
                        'success':'False',
                        'message':'Already Blocked'
                        },status=HTTP_400_BAD_REQUEST)


class UnblockUserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        user_id = self.kwargs['pk']
        try:
            user=User.objects.get(id=user_id)
        except:
            return Response({
                'success':'False', 
                'message':'No user to unblock'
                },status=HTTP_400_BAD_REQUEST)
                
        if user.is_active == False:
            user.is_active = True
            user.save()
            return Response({
                        'success':'True',
                        'message':'User unblocked successfully'
                        },status=HTTP_200_OK)
        else:
            return Response({
                        'success':'False',
                        'message':'Already unblocked'
                        },status=HTTP_400_BAD_REQUEST)


class UserProfileDetailsAPIView(APIView):
    def get(self,request,*args,**kwargs):
        user_id =  self.kwargs['pk']
        
        try:
            obj = UserOtherInfo.objects.get(user__id=user_id)
        except:
            return Response({
                'success' : 'False',
                'message' : 'No user found',
            },status=HTTP_404_NOT_FOUND)

        serializer = UserDetailsSerializer(obj)
        data = serializer.data  
        return Response({
            'success'  :'True',
            'message'  : 'Data retrieved successfully',
            'data'     : data  
        },status=HTTP_200_OK)


class DeleteUserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        
        user_id = self.kwargs['pk']
        print('user_id',user_id)
        try:
            obj = User.objects.get(id=user_id)
        except:
            return Response({
                'success' : 'False',
                'message' :'No user to delete'
                },status=HTTP_400_BAD_REQUEST)

        obj.delete()
        return Response({
            'success' : 'True',
            'message' : 'User deleted successfully',
        },status=HTTP_200_OK)


class StudentModelViewSet(viewsets.ModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

'''
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

'''
