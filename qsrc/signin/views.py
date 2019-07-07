# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout,login
from applet import views
# Create your views here.
def registration(request):
    if request.method=='POST':
        form1=userform(request.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            first_name=form1.cleaned_data['first_name']
            last_name=form1.cleaned_data['last_name']
            email=form1.cleaned_data['email']
            password=form1.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            return HttpResponseRedirect('/upload/start')
    else:
        form1=userform()
    return render(request,'registration.html',{'frm':form1})

def login(request):
    '''if request.user.is_autheticated():
        return redirect('offerride/index.html')'''
    if request.method=="POST":
        username =request.POST['user']
        password=request.POST['pas']
        try:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return render(request,'welcome.html')
            else:
                messages.error(request,'Username and password did not match')
        except auth.ObjectNotExist:
            print("invalid user")
    return render(request,'login.html')


def logout(request):
    #logout(request)
    #return redirect('offerride/index.html')

    auth.logout(request)
    
    return render(request, 'login.html')

def admin_page(request):
    if not request.user.is_autheticated():
        return redirect('signin/login.html')

    return  render(request, 'offerride/index.html')


def profile(request):
    prof = User.objects.all()
    context={
        'profile': prof
    }
    return render(request,'profile.html',context)

def email(request):
    subject = 'ride confirmation'
    k = 'hello'
    email_from = settings.EMAIL_HOST_USER
    rel= 'ankichan1812@gmail.com'
    send_mail(subject, k, email_from, [rel],fail_silently=False)
    return render(request,'send.html')