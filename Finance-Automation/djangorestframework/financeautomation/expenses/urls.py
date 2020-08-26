from django.urls import path
from expenses.views import(
    all_api_paths,
    expense_list,
    expense_detail,
)

urlpatterns = [
    path('',all_api_paths, name='All Api Paths'),
    path('expense_list', expense_list, name='expense_list api'),
    path('expense_detail/<int:pk>', expense_detail, name='expense_detail')
]