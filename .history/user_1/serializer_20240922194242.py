from rest_framework import serializers
from user_1.models import Registrationform,Doctors,Patients,Staffs,Booking

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
     model=Registrationform
     fields='__all__'
class DSerializer(serializers.ModelSerializer):
    class Meta:
     model=Registrationform
     fields='__all__'