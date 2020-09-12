from django.urls import path, include
from users.views import(
    # login,
    register,
    index
)

urlpatterns = [
    path('', index, name='Index'),
    path('register', register, name='Register')
]