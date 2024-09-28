from django.urls import path
from .views import Registration,login

urlpatterns = [
    path('register/', Registration, name='register'),
    # path('login',login,name='loginform'),