from django.contrib import admin
from crudapp.models import *
# Register your models here.

class StudentDisplay(admin.ModelAdmin):
    list_display = ['name','email','phone','age']


admin.site.register(Student,StudentDisplay)
