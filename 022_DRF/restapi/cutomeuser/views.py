from django.shortcuts import render
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from cutomeuser.models import *
from cutomeuser.serializer import *
from rest_framework.permissions import AllowAny
from cutomeuser.serializer import *
from cutomeuser.permission import *
# Create your views here.


@api_view(['POST'])
@permission_classes([])
def reg_user(request):
    ser = UserSerilaizer(data = request.data)
    if not ser.is_valid():
        print(ser.errors)
    else : 
        ser.save()
    return Response("ok")

@api_view(['GET'])
@permission_classes([IsStudent])
def studentapi(request):
    return Response({"message":"student api calling"})


@api_view(['GET'])
@permission_classes([IsFaculty])
def facultyapi(request):
    return Response({"message":"faculty api calling"})