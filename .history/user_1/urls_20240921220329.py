from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.Registration, name='register'),
    # path('login',login,name='loginform'),
]