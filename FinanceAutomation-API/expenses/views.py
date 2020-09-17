from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from expenses.serializers import ExpenseSerializer

# Create your views here.
def expenses_dashboard(request):
    return HttpResponse("You are looking for a dashboard for all the expenses")

# adding a single expense at a time
def add_expense(request):
    # Checking if user is authenitcated
    if request.user.is_authenticated:
        # Checking if the user is a staff member
        if request.user.is_staff:
            if request.method == "POST":
                return HttpResponse("You are posting something!")
            elif request.method == "GET":
                return render(
                    request = request,
                    template_name="expenses/add-expense.html",
                    context={"user":request.user}
                )
        return HttpResponse("You are not a staff")
    else:
        return redirect("login_user")

        