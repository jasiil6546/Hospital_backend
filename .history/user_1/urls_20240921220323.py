from django.urls import path
from . import views

urlpatterns = [
    path('register/',viwsRegistration, name='register'),
    # path('login',login,name='loginform'),
]