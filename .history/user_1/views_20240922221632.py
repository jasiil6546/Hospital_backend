from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password,check_password
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
        User_name = request.POST.get('username')
        Password = request.POST.get('password')

        
        if request.session.get('user_id'):
            return JsonResponse({
                'message': 'User already logged in',
                'status': 'success',
            })

        
        try:
            user = Registrationform.objects.get(USER_NAME=User_name)
            if check_password(Password, user.PASSWORD):
                
                response = JsonResponse({'success': 'Login successfully'})

                
                request.session['user_name'] = user.USER_NAME
                request.session['user_id'] = user.id
                response.set_cookie('login_cookie', 'cookie_value', max_age=3600)

                
                csrf_token = get_token(request)
                response.set_cookie('csrftoken', csrf_token)

                return response
            else:
                return JsonResponse({'error': 'Password is incorrect'})
        except Registrationform.DoesNotExist:
            return JsonResponse({'error': 'Username not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
@csrf_exempt 
def logouts(request):
    
    logout(request)
    response= JsonResponse({'message':'logout successfully'})
    response.delete_cookie('login_cookie')
    response.delete_cookie('csrftoken')
    

    return response

def data_of_Doctors(request):
   if request.method=="POST":
      Name = request.POST.get('name')
      User_name=request.POST.get('username')
      Password = request.POST.get('password')
      Email = request.POST.get('email')
      Category=request.POST.get('category')
      Phone_number = request.POST.get('phone')
      Age = request.POST.get('age')
      Gender = request.POST.get('gender')
      
      if Doctors.objects.filter(USER_NAME=User_name).exists():
    