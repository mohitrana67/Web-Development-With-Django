from django.urls import path

from .views import *

urlpatterns = [
    path('<int:user_id>', home_view, name='accounting_home_view'),

    path('<int:user_id>/add_accouting_expense', add_accounting_expense, name='add_accounting_expense'),

    path('<int:user_id>/expenses_list', expenses_list, name='accounting_expense_list'),

    path('<int:user_id>/add_csv_data', add_csv_data, name='add_csv_data'),

    path('loadReact', loadReact, name="loadReact")

]