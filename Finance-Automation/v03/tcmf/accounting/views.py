from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import *
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
    expense_list = [{"id":x.id,"expense_name":x.expense_name,"expense_amount":x.expense_amount} for x in expenses]
    data["response"] = expense_list()

    return JsonResponse(data,status=200)