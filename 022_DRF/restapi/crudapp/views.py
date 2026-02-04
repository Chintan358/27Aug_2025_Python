from django.shortcuts import render
from rest_framework.decorators import APIView,api_view,permission_classes
from rest_framework.response import Response
from crudapp.models import *
from crudapp.serializer import *
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from crudapp.permissions import IsSuperUser
# Create your views here.
class AuthorAPI(APIView):

    
    @permission_classes([IsAuthenticated])
    def get(self,request):
        authors = Author.objects.all()
        ser = AuthorSerializer(authors,many=True)
        return Response({"data":ser.data})

    @permission_classes([IsSuperUser])
    def post(self,request):
        ser = AuthorSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})
    
class AutherUpdateAPI(APIView):   


    @permission_classes([IsAuthenticated])
    def get(self,request,id):
        author = Author.objects.get(pk=id)
        ser  = AuthorSerializer(author)
        return Response({"data":ser.data})
    
    @permission_classes([IsSuperUser])
    def delete(self,request,id):
        author = Author.objects.get(pk=id)
        author.delete()
        return Response({"message":"author deleted"})
    
    @permission_classes([IsSuperUser])
    def put(self,request,id):
        author = Author.objects.get(pk=id)
        ser = AuthorSerializer(author,request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})
        

@api_view(['POST'])
@permission_classes([IsSuperUser])
def addbook(request,id):
    data = request.data
    data.update({"author":id})
    ser = BookSerializer(data= data)
    if not ser.is_valid():
            return Response({"errors":ser.errors})
    else:
            ser.save()
            return Response({"data":ser.data})
    
@api_view(["GET"])
@permission_classes([AllowAny])
def viewbook(request):
    books = Book.objects.all()
    ser = BookSerializer(books,many=True)
    return Response({"data":ser.data})    


class BookById(APIView):
     
     @permission_classes([IsAuthenticated])
     def get(self,request,id):
        books = Book.objects.get(pk=id)
        ser =  BookSerializer(books)
        return Response({"data":ser.data})
     
     @permission_classes([IsSuperUser])
     def delete(self,request,id):
        books = Book.objects.get(pk=id)
        books.delete()
        return Response({"message":"book deleted"})
     
@api_view(['PUT'])
@permission_classes([IsSuperUser])
def updatebook(request,id, bid):
    data = request.data
    data.update({"author":id})
    cdata = Book.objects.get(pk=bid)
    ser = BookSerializer(cdata,data)
    if not ser.is_valid():
            return Response({"errors":ser.errors})
    else:
            ser.save()
            return Response({"data":ser.data})