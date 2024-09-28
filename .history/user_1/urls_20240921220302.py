from django.urls import path
from . import

urlpatterns = [
    path('register/',Registration, name='register'),
    # path('login',login,name='loginform'),
]