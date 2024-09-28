from django.urls import path
from . import views

urlpatterns = [
    path('register',views.Registration, name='register'),
    path('login',views.login,name='loginform'),
    path('logout',views.logouts,name='logout'),
    path('datadoc',views.data_of_Doctors,name="Doctor"),
    path('datastaff',views.data_of_Staffs,name="staff"),
    path('datapatient',views.data_of_Patients,name="patient"),
    path('booking',views.booking,name='booking'),
    path('delbook',views.deletebooking,name="deletebooking"),
    path('deldata',views.delete_data,name='delete_data'),
    path('displaydoc',views.diplay_details_of_doctors,name='doctor'),
    path('displaystaff',views.display_staffs,name='staffs'),
    path('displaypatients',views.display_Patients,name='patients'),
    path('search/<str:name',views.search_doctor,name='search'),
    path('seaar')
 ]