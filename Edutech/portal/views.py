from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from serializer import *

# from rest_framework import request


# Create your views here.
@api_view(['GET'])
def student_profile(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serialize = StudentSerializer(student, many=True)
        return Response(serialize.data)