from django.urls import path

from .views import *

urlpatterns = [
    # dispatching/1 index page for accounting
    path('<int:user_id>', home_view, name='accounting_home_view'),

    # dispatching/1/add_accounting_expense for accounting
    path('<int:user_id>/add_accouting_expense', add_accounting_expense, name='add_accounting_expense'),

    # dispatching/1/expense_list page for showing the expense list
    path('<int:user_id>/expenses_list', expenses_list, name='accounting_expense_list'),

    # dispatching/1/add_csv_data page for adding csv data
    path('<int:user_id>/add_csv_data', add_csv_data, name='add_csv_data'),

    # dispatching/1/add_csv_data page for adding csv data
    path('<int:user_id>/add_csv_expense', add_csv_expense, name='add_csv_expense'),
]