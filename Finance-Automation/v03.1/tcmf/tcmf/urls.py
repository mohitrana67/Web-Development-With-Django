"""
tcmf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dispatching.views import *
from accounting.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dispatching/home/<int:dispatcher_id>', trip_home_view, name="dispatching_home"),
    path('dispatching/trip/<int:dispatcher_id>/<int:trip_id>', trip_data, name="dispatching_trip_data"),
    path('dispatching/trips', trips_list, name="dispatching_trip_list"),
    path('dispatching/trip/add',create_trip, name="dispatching_create_trip"),
    path('accounting/home/<int:accontant_id>',accounting_home_view, name="accounting_home_view"),
    path('accounting/expense_list',accounting_expense_list_view, name='accounting_expense_list_view'),
    path('accounting/add_expense',accounting_add_expense, name='accounting_add_expense')
]
 