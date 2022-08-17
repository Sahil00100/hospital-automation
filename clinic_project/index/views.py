from django.shortcuts import render,redirect
import random
# Create your views here.
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required  
from.models import *
# Create your views here.


def login_view(request):
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            
            messages.add_message(request, messages.ERROR, 'Username or Password is invalid')
            print('invalid username or password')
            return redirect('login')
    
    return render(request,'login.html',{})
@login_required(login_url='login')
def middle_view(request):

    return render(request,'middle.html',{})
@login_required(login_url='login')
def new_patient_view(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phone')
        house=request.POST.get('house')
        city=request.POST.get('city')
        district=request.POST.get('district')
        state=request.POST.get('state')
        age=request.POST.get('age')
        symptom=request.POST.get('symptoms')
        disease=request.POST.get('disease')
        med=request.POST.get('med')
        code=random.randrange(10000,99999)
        print(code)
        if Patient.objects.filter(code=code).exists():
            code=random.randrange(10000,99999)
            p=Patient(
            name=name,
            email=email,
            phonenumber=phonenumber,
            house=house,
            city=city,
            district=district,
            state=state,
            age=age,
            symptoms=symptom,
            disease=disease,
            medicine=med,
            date=datetime.datetime.today(),
            code=code,
            )
            p.save()

            return redirect('result',code)
        else:
            p=Patient(
                name=name,
                email=email,
                phonenumber=phonenumber,
                house=house,
                city=city,
                district=district,
                state=state,
                age=age,
                symptoms=symptom,
                disease=disease,
                medicine=med,
                date=datetime.datetime.today(),
                code=code,
            )
            p.save()

            return redirect('result',code)
    return render(request, 'index.html',{})

@login_required(login_url='login')
def patient_login(request):
    if request.method=="POST":
        code=request.POST['code']
        if Patient.objects.filter(code=code).exists():
            return redirect('view',code)
        else:
            return redirect('patient')
    return render(request,'patient.html',{})

@login_required(login_url='login')
def patient_view(request,code):
    p=Patient.objects.get(code=code)
    return render(request,'medicine.html',{'p':p})

#log out
def logout_view(request):
    logout(request)
    print('logout success!')
    return redirect('login')

def result(request,code):
    
    return render(request,'result.html',{'code':code})