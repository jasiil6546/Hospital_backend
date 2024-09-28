from django.db import models

# Create your models here.
class Registrationform(models.Model):
    NAME = models.CharField(max_length=90)
    PASSWORD = models.CharField(max_length=100)  
    EMAIL = models.EmailField(max_length=90)
    PHONE_NUMBER = models.CharField(max_length=11)
    CATEGORY = models.CharField(max_length=20)  
    AGE = models.PositiveIntegerField(max_length=200)
    GENDER = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return"{} {} {}".format(self.NAME,self.PASSWORD,self.EMAIL,self.PHONE_NUMBER,self.AGE,self.GENDER,self.created_at)
