from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serializer import *
# Create your views here.

@api_view(['GET'])
def get_api(request):
    return Response({"meg":"GET API calling"})


@api_view(['POST'])
def post_api(request):
    return Response({"meg":"POST API calling"})


@api_view(['PUT'])
def put_api(request):
    return Response({"meg":"PUT API calling"})


@api_view(['DELETE'])
def delete_api(request):
    return Response({"meg":"DELETE API calling"})


@api_view(['GET'])
def students(request):
    students = Student.objects.all()
    ser = StudentSerializer(students,many=True)
    return Response({"data":ser.data})

@api_view(['POST'])
def add_students(request):
    ser = StudentSerializer(data=request.data)
    if not ser.is_valid() : 
        return Response({"Errors":ser.errors,"message":"Something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Student inserted successfully"})
    
@api_view(['PUT'])
def update_students(request,id):
    std = Student.objects.get(pk=4)
    ser = StudentSerializer(std,request.data,partial=True)
    if not ser.is_valid() : 
        return Response({"Errors":ser.errors,"message":"Something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Student updated successfully"})
    
@api_view(['DELETE'])
def delete_students(request,id):
    std = Student.objects.get(pk=4)
    std.delete()
    return Response({"message" :"Student delete"})