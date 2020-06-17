from django.urls import path

from users.views import *

urlpatterns = [
    # view for home page
    path('index', home_view, name='user_index_view'),

    # API urls
    path('create_user', create_user, name='user_create_user')

]