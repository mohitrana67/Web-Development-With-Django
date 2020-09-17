from django.urls import path
from accounts.views import (
    register_user,login_user, profile,logout_user, register_api
)

urlpatterns = [
    path('register',register_user, name='register_user'),
    path('login', login_user, name='login_user'),
    path('profile', profile, name="profile"),
    path('logout', logout_user, name='logout_user'),
    # From here we will work on api endpoints
    path('register_api', register_api, name="register_api")
] 