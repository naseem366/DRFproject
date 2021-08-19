from django.shortcuts import render
import io
import requests
from rest_framework.parsers import JSONParser 
from rest_framework.renderers import JSONRenderer 
from .serializers import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method =='POST':
        json_data=request.body()
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parser(stream)
        data1=StudentSerializer(data=pythondata)
        if data1.is_valid():
            data1.save()
            res={'msg':'hello data'}
            json_data=JSONRenderer().renderer(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().renderer(data1.errors)
        return HttpResponse(json_data,content_type='application/json')

