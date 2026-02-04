from rest_framework.permissions import BasePermission
from cutomeuser.models import CustomeUser
class IsStudent(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.role.name=='Student'
    
class IsFaculty(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.role.name=='Faculty'