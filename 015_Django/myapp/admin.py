from django.contrib import admin
from myapp.models import *
# Register your models here.

class StudentData(admin.ModelAdmin):
    list_display = ["name","email","phone","age"]

admin.site.register(Student,StudentData)
