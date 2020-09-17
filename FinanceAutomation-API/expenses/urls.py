from django.urls import path

from expenses.views import (
    expenses_dashboard,
    add_expense
)

urlpatterns = [
    path('expenses-dashboard', expenses_dashboard, name='expenses-dashboard'),
    path('add_expense', add_expense, name="add_expense"),
]