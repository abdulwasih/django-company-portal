from django.contrib.auth import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from employeeprofile.tables import EmployeeTable
from .models import Employee

from employeeprofile.models import Employee
from .forms import EmployeeForm

def home(request):
    return render(request, 'employeeprofile/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'employeeprofile/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'employeeprofile/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'employeeprofile/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'employeeprofile/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'employeeprofile/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('loggeduser')

def emplog(request):
    return render(request,'employeeprofile/employeelogin.html')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def loggeduser(request):
    return render(request,'employeeprofile/loggeduser.html')

@login_required
def registeremp(request):
    form  = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'employeeprofile/registeremployee.html',{'form':EmployeeForm()})

@login_required
def viewemp(request):
    table = Employee.objects.all()
    return render(request,'employeeprofile/viewemployees.html',{'table':table})

# def emplogin(request):
#     # user = Employee.objects.filter(empid=request.GET.get('empid') ,password=request.GET.get('password'))
#     return render(request,'employeeprofile/profile.html')

def emplogin(request):
    user = Employee.objects.filter(empid=request.GET.get('empid') ,password=request.GET.get('password'))
    return render(request,'employeeprofile/profile.html',{'user':user})

# def convert(request):

#     word = ''

#     inputnum = request.GET.get('num')
#     word = num2words(inputnum).capitalize()
  

#     return render(request, 'converter/convert.html', {'word':word})

