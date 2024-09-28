from rest_framework import serializers
from user_1.models import Registrationform

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
     model=Registrationform
     fields='__all__'
     