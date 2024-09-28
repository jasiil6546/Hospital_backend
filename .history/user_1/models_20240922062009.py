from django.db import models

# Create your models here.
class Registrationform(models.Model):
    NAME = models.CharField(max_length=90)
    USER_NAME=models.
    PASSWORD = models.CharField(max_length=100)  
    EMAIL = models.EmailField(max_length=90)
    PHONE_NUMBER = models.CharField(max_length=11)
    CATEGORY = models.CharField(max_length=500)  
    AGE = models.PositiveIntegerField()
    GENDER = models.CharField(max_length=(20))
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return"{} {} {}".format(self.NAME,self.PASSWORD,self.EMAIL,self.PHONE_NUMBER,self.CATEGORY,self.AGE,self.GENDER,self.created_at)
class Doctors(models.Model):
    NAME = models.CharField(max_length=90)
    PASSWORD = models.CharField(max_length=90)  # Hash the password before storing it
    EMAIL = models.EmailField(max_length=50)
    PHONE_NUMBER = models.CharField(max_length=11)
    CATEGORY = models.CharField(max_length=200)
    AGE = models.PositiveIntegerField()  # Use PositiveIntegerField for age
    GENDER = models.CharField(max_length=10)  # Added choices for gender
    created_at = models.DateTimeField(auto_now_add=True)   


class Staffs(models.Model):
    NAME = models.CharField(max_length=90)
    PASSWORD = models.CharField(max_length=90)  # Hash the password before storing it
    EMAIL = models.EmailField(max_length=50)
    PHONE_NUMBER = models.CharField(max_length=11)
    CATEGORY = models.CharField(max_length=200)
    AGE = models.PositiveIntegerField()  # Use PositiveIntegerField for age
    GENDER = models.CharField(max_length=10)  # Added choices for gender
    created_at = models.DateTimeField(auto_now_add=True) 

class Booking(models.Model):
    NAME = models.CharField(max_length=90)
    PASSWORD = models.CharField(max_length=90)  # Hash the password before storing it
    EMAIL = models.EmailField(max_length=50)
    PHONE_NUMBER = models.CharField(max_length=11)
    CATEGORY = models.CharField(max_length=200)
    AGE = models.PositiveIntegerField()  # Use PositiveIntegerField for age
    GENDER = models.CharField(max_length=10)  # Added choices for gender
    created_at = models.DateTimeField(auto_now_add=True)  
 
class Patients(models.Model):
    NAME = models.CharField(max_length=90)
    PASSWORD = models.CharField(max_length=90)  # Hash the password before storing it
    EMAIL = models.EmailField(max_length=50)
    PHONE_NUMBER = models.CharField(max_length=11)
    CATEGORY = models.CharField(max_length=200)
    AGE = models.PositiveIntegerField()  # Use PositiveIntegerField for age
    GENDER = models.CharField(max_length=10)  # Added choices for gender
    created_at = models.DateTimeField(auto_now_add=True)
    