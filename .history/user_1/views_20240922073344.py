from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse,HttpResponse
from user_1.serializer import RegisterSerializer
from .models import Registrationform,Doctors,Staffs,Booking,Patients
# Create your views here.
@csrf_exempt
def Registration(request):
    if request.method =='POST':
            Name = request.POST.get('name')
            User_name=request.POST.get('username')
            Password = request.POST.get('password')
            Email = request.POST.get('email')
            Category=request.POST.get('category')
            Phone_number = request.POST.get('phone')
            Age = request.POST.get('age')
            Gender = request.POST.get('gender')
            if Registrationform.objects.filter(USER_NAME=User_name).exists(): 
                return JsonResponse({'error':'user_name already exists'})
            else:
                if Category == "Doctors":
                    Doctors.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=Password,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    Registrationform.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=Password,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    
                    return JsonResponse({'status':'sucess'})
                elif Category == "Staffs":
                    Staffs.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=Password,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    Registrationform.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=Password,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    return JsonResponse({'status':'sucess'})
                else:
                    Patients.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=Password,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    Registrationform.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=Password,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                
                    return JsonResponse({'status':'sucess'})
    else:  
         return JsonResponse({'error':"no data"})
      
def login(request):
    User_name= request.post.get('user_name')
    Password = request.post.get('password')                       
    if Registrationform.objects.filter(USER_NAME=User_name,PASSWORD=Password).exists():
            return HttpResponse("Success")
    else:
             return HttpResponse("Failed")