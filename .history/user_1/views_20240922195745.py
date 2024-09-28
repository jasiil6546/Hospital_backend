from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse,HttpResponse
from .serializer import RegisterSerializer,DoctorsSerializer,PatientsSerilizers,StaffsSerializer
from .models import Registrationform,Doctors,Staffs,Booking,Patients
from django.contrib.auth import login,logout,authenticate
from django.middleware.csrf import get_token
# Create your views here.
def get_csrf_token(request):
    csrf_token=get_token(request)
    return JsonResponse({"csrftoken":csrf_token})
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
                    Registrationform.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=make_password(Password),EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    
                    return JsonResponse({'status':'sucess'})
                elif Category == "Staffs":
                    Staffs.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=Password,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    Registrationform.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=make_password(Password),EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    return JsonResponse({'status':'sucess'})
                else:
                    Patients.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=Password,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    Registrationform.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=make_password(Password),EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                
                    return JsonResponse({'status':'sucess'})
    else:  
                    return JsonResponse({'error':"no data"})
 
@csrf_exempt     
def login(request):
 if request.method == 'POST':
    User_name= request.POST.get('username')
    Password = request.POST.get('password')   
    if request.session.get('user_id'):

            return JsonResponse({
                'message':'User already logged in',
                'status':'success',
                'username': request.session.get('phone')
            })                    
    if Registrationform.objects.filter(USER_NAME=User_name,PASSWORD=Password).exists():
      return HttpResponse("LOGiN SUCCESFULLY")
    else:
      return HttpResponse("Failed")