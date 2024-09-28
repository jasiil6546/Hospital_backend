from django.urls import path
from . import views

urlpatterns = [
    path('register',views.Registration, name='register'),
    path('login',views.login,name='loginform'),
    path('logout',views.logouts,name='logout'),
    path
]