from django.urls import path
from myapp.views import *

urlpatterns = [
    path("get-api",get_api,name="get-api"),
    path("post-api",post_api,name="post-api"),
    path("put-api",put_api,name="put-api"),
    path("delete-api",delete_api,name="delete-api"),


    path("students",students,name="students"),
    path("add-students",add_students,name="add-students"),


  path("update-students/<id>",update_students,name="update-students"),

  path("delete-students/<id>",delete_students,name="delete-students"),
]
