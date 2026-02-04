from django.urls import path
from cutomeuser.views import *


urlpatterns = [
    path("reg",reg_user,name="reg"),
    path("student",studentapi,name="student"),
    path("faculty",facultyapi,name="faculty")
]