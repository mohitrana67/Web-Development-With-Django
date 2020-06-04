from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

from .models import *
from .forms import *

# Create your views here.
def accounting_home_view(request,*args,**kwargs):
    return render(
        request = request,
        template_name = "accounting/home.html",
        context=None,
        content_type = None
    )


def accounting_expense_list_view(request,*args,**kwargs):
    data = {}
    expenses = Expense.objects.all()
    expense_list = [{
        "id":x.id,
        "expense_account_type":x.expense_account_type,
        "expense_transaction_date":x.expense_transaction_date,
        "expense_name":x.expense_name,
        "expense_description_1":x.expense_description_1,
        "expense_description_2":x.expense_description_2,
        "expense_amount_cad":x.expense_amount_cad,
        "expense_amount_usd":x.expense_amount_usd,
        "expense_gst":x.expense_gst,
        "expense_pst":x.expense_pst,
        "expense_pvt":x.expense_pvt
        } for x in expenses]
    data["response"] = expense_list

    return JsonResponse(data,status=200)


def accounting_add_expense(request,*args,**kwargs):
    # We will create an object for the form class
    form = AddExpense(request.POST or None)

    next_url = request.POST.get("next") or None
    
    # check if we are getting any data alreadt in the request
    if form.clean_content():
        obj = form.save(commit=False)
        obj.save()
        # creating an empty form
        form = AddExpense()
        
        # return HttpResponse("You are here")
    return render(
        request = request,
        template_name = "components/accounting/expense_form.html",
        context = {"form":form}
    )