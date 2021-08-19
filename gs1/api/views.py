from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.
def std_detail(request):
    stu=Student.objects.get(id=3)
    #print(stu)
    data=StudentSerializer(stu).data
    #print(data)
    #json_data=JSONRenderer().render(data)
    #print(json_data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(data)
    