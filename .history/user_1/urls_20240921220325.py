from django.urls import path
from . import views

urlpatterns = [
    path('register/',viws.Registration, name='register'),
    # path('login',login,name='loginform'),
]