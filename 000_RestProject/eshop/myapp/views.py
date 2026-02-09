from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from myapp.models import *
from myapp.serializer import *
from rest_framework.permissions import AllowAny,IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [IsAdminUser]

        # GET USER BY ID -> anyone allowed
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]

        # CREATE USER -> login required
        elif self.action == 'create':
            permission_classes = [AllowAny]

        # UPDATE USER -> admin only
        elif self.action == 'update':
            permission_classes = [IsAuthenticated]

        # PARTIAL UPDATE -> admin only
        elif self.action == 'partial_update':
            permission_classes = [IsAuthenticated]

        # DELETE USER -> admin only
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(
            {
                "status": True,
                "message": "User deleted successfully"
            },
            status=status.HTTP_200_OK
        )

class CategoryViewSet(ModelViewSet):

    queryset =Category.objects.all()
    serializer_class = CategorySerializer



    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [AllowAny]

       
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]

     
        elif self.action == 'create':
            permission_classes = [IsAdminUser]

        
        elif self.action == 'update':
            permission_classes = [IsAdminUser]

        elif self.action == 'partial_update':
            permission_classes = [IsAdminUser]

       
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]

        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(
            {
                "status": True,
                "message": "Category deleted successfully"
            },
            status=status.HTTP_200_OK
        )
    

class ProductViewSet(ModelViewSet):

    queryset =Product.objects.all()
    serializer_class = ProductSerializer



    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [AllowAny]

       
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]

     
        elif self.action == 'create':
            permission_classes = [AllowAny]

        
        elif self.action == 'update':
            permission_classes = [AllowAny]

        elif self.action == 'partial_update':
            permission_classes = [AllowAny]

       
        elif self.action == 'destroy':
            permission_classes = [AllowAny-]

        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(
            {
                "status": True,
                "message": "Category deleted successfully"
            },
            status=status.HTTP_200_OK
        )
