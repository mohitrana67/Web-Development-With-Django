from django.urls import path

from .views import *

urlpatterns = [
    # dispatching/ index page for accounting
    path('<int:userId>', home_view, name='accounting_home_view'),
]