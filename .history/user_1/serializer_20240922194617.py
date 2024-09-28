from rest_framework import serializers
from user_1.models import Registrationform,Doctors,Patients,Staffs,Booking

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
     model=Registrationform
     fields='__all__'
class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
     model=Doctors
     fields='__all__'
class PatientsSerilizers(serializers.ModelSerializer):
    class Meta:
     model=Patients
     fields='__all__'
     
class StaffsSerializer(serializers.ModelSerializer):
    class Meta:
     model=
     fields='__all__'