from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Account, CustomAccountManager
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import status

from accounts.serializers import AccountSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# Registering A new user
def register_user(request):
    if request.method == 'GET':
        return render(
            request = request,
            template_name= 'accounts/register.html',
        )
    elif request.method == 'POST':
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        if password1 != password2:
            return render(
                request=request,
                template_name = 'accounts/register.html',
                context = {"message": "Password Doesn't match"}
            )
        else:
            user = Account.objects.create_user(email=email,username = username, password=password1, first_name=first_name, last_name=last_name, user_type=1)                
            return render(
                request=request, 
                template_name="accounts/register.html",
                context = {"message":f"User Create with username {username}"}
            ) 

# Login a new user
def login_user(request):
    if request.method == "GET":
        #we need to implement a functionality to check if user is alreadt logged in
        #for now we will just show a new login page every time
        return render(
            request=request,
            template_name="accounts/login.html",
        )
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            """Here we have to implement following Functionalities
                1. Login the user and give user a session id.
                2. Redirect user to a Profile page he has.
            """
            
            # to login a user and assign a session to a user 
            login(request, user)

            return redirect('profile')
        else:
            return HttpResponse("Username and password doesn't match")

# User Profile
def profile(request,**kwargs):
    if request.user.is_authenticated:
        return render(request=request,template_name='accounts/profile.html',context={"user":request.user})
    else:
        return HttpResponse("Please login First to see the user profile")

# Logout
def logout_user(request):
    logout(request)
    return HttpResponse("You are logged out")

""" We will create all the API's from here """

# API for creating a new user
@api_view(['POST','GET'])
def register_api(request):
    if request.method == 'GET':
        return Response({"data":"You wanna register a new user"})
    elif request.method == 'POST':
        data = request.data
        
        if request.data.get("password") != request.data.get("password1"):
            return Response({"error":"Please enter same password"})
        else:
            if len(request.data.get("password")) < 5:
                return Response({"error": "please enter a password more than 5 characters"})

            data = {
                "email":request.data.get("email"),
                "username": request.data.get("username"),
                "first_name":request.data.get("first_name"),
                "last_name":request.data.get("last_name"),
                "password":request.data.get("password")
            }

            account = AccountSerializer().create(data)

            return Response({"user":account})

