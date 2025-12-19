from django.shortcuts import render
from crudapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        age = data.get("age")
        Student.objects.create(name=name,email=email,phone=phone,age=age)
    return render(request,'index.html',{"msg":"Registration successfully !!!"})

def display(request):
    students = Student.objects.all()
    return render(request,"display.html",{"students":students})