from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from myapp.models import *
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,"index.html")

def addstudent(request):
    if request.method=="POST":
        name = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']


    Student.objects.create(name=name,email=email,phone=phone)
    return HttpResponse("Student added successfully !!!")

def display(request):
    students = Student.objects.all()
    return JsonResponse({"students":list(students.values())})

def delete_student(request):
    sid = request.GET['sid']
    student = Student.objects.get(pk=sid)
    student.delete()
    return HttpResponse("Student Deleted !!!")

def getbyid(request):
    sid = request.GET['sid']
    student = Student.objects.filter(id=sid)
    return JsonResponse({"student":list(student.values())})


def updatestudent(request):
    if request.method=="POST":
        id = request.POST["id"]
        name = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']

        student = Student.objects.get(pk=id)
        student.name = name
        student.email = email
        student.phone = phone
        student.save()


    
        return HttpResponse("Student update successfully !!!")
    
def search(request):
    q = request.GET['q']
    # students = Student.objects.filter(name__startswith=q ) or Student.objects.filter(email__startswith=q ) or Student.objects.filter(phone__startswith=q )

    students = Student.objects.filter(Q(name__startswith=q)|Q(phone__startswith=q)|Q(email__startswith=q)) 
    return JsonResponse({"students":list(students.values())})
