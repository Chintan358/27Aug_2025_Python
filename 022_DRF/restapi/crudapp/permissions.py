from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser