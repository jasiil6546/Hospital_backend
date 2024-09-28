from django.urls import path
from . import views

urlpatterns = [
    path('register',views.Registration, name='register'),
    path('login',views.login,name='loginform'),
    path('logout',views.logouts,name='logout'),
    path('datadoc',views.data_of_Doctors,name="Doctor"),
    path('datastaff',views.data_of_Staffs,name="staff"),
    path('datapatient',views.data_of_Patients,name="patient"),
    
]