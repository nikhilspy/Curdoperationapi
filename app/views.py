from turtle import update
from django.shortcuts import render,redirect
from .models import *
from django.template import RequestContext
# Create your views here.

def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']



    newuser = Student.objects.create(Firstname=fname,Lastname=lname, Email=email,Contact=contact)

    return redirect('showpage')

def ShowPage(request):

    all_data = Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})  

def EditPage(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})


def UpdateData(request,pk):
    udate = Student.objects.get(id=pk)
    udate.Firstname = request.POST['fname']
    udate.Lastname = request.POST['lname']
    udate.Email = request.POST['email']
    udate.contact = request.POST['contact']

    udate.save()
    return redirect('showpage')


def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)

    ddata.delete()
    return redirect('showpage')