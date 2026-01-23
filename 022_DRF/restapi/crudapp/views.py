from django.shortcuts import render
from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response
from crudapp.models import *
from crudapp.serializer import *
# Create your views here.
class AuthorAPI(APIView):

    def get(self,request):
        authors = Author.objects.all()
        ser = AuthorSerializer(authors,many=True)
        return Response({"data":ser.data})

    def post(self,request):
        ser = AuthorSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})
    
class AutherUpdateAPI(APIView):   



    def get(self,request,id):
        author = Author.objects.get(pk=id)
        ser  = AuthorSerializer(author)
        return Response({"data":ser.data})
    
    def delete(self,request,id):
        author = Author.objects.get(pk=id)
        author.delete()
        return Response({"message":"author deleted"})
    
    def put(self,request,id):
        author = Author.objects.get(pk=id)
        ser = AuthorSerializer(author,request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})
        

@api_view(['POST'])
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
def viewbook(request):
    books = Book.objects.all()
    ser = BookSerializer(books,many=True)
    return Response({"data":ser.data})    