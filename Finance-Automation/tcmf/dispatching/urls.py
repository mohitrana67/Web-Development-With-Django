from django.urls import path

from dispatching import views

urlpatterns = [
    # dispatching/ index page for accounting
    path('<int:userId>', views.index, name='dispatching_index'),

    # dispatching/addTrip
    path('addTrip', views.addTrip, name='dispatching_addTrip'),
]
