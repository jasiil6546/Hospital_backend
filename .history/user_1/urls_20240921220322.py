from django.urls import path
from . import views

urlpatterns = [
    path('register/',viRegistration, name='register'),
    # path('login',login,name='loginform'),
]