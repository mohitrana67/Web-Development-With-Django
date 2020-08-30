from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
from users.serializers import RegisterationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return HttpResponse("You are at index")

@api_view(['POST',])
def register(request):
    if request.method == 'POST':
        serializer = RegisterationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["reesponse"] = "Data Registered as requested"
            data["email"] = user.email
            data["username"] = user.username
        else:
            data = serializer.errors
        return Response(data)
#     if request.method == 'POST':
#         email = request.POST.get("email")
#         username = request.POST.get("username")
#         fname = request.POST.get("fname")
#         lname = request.POST.get("lname")
#         age = request.POST.get("age")
#         password = request.POST.get("password")

#         user = User.objects.create_user(email=email, username=username, first_name=fname, last_name=lname, age=age, password=password)

#         return HttpResponse(f"{email}, {username}, {fname}, {lname}, {age}")
#     elif request.method == 'GET':
#         return render(request, 'users/register.html')

