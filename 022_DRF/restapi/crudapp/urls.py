from django.urls import path
from crudapp.views import *

urlpatterns = [

    path("authors",AuthorAPI.as_view()),
    path("authors/<id>",AutherUpdateAPI.as_view()),

    path("books/author/<id>",addbook,name="addbook"),
     path("books/author/<id>/<bid>",updatebook,name="updatebook"),
    path("books",viewbook,name="books"),
    path("books/<id>",BookById.as_view())
]