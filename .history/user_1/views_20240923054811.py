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
                    Doctors.objects.create(NAME=Name,USER_NAME=User_name,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    Registrationform.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=make_password(Password),EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    
                    return JsonResponse({'status':'sucess'})
                elif Category == "Staffs":
                    Staffs.objects.create(NAME=Name,USER_NAME=User_name,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    Registrationform.objects.create(NAME=Name,USER_NAME=User_name,PASSWORD=make_password(Password),EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
                    return JsonResponse({'status':'sucess'})
                else:
                    Patients.objects.create(NAME=Name,USER_NAME=User_name,EMAIL=Email,CATEGORY=Category,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
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

@csrf_exempt
def booking(request):
    if request.method=='POST':
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Phone=request.POST.get('date_of_birth')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        email=request.POST.get('email')
        doctor=request.POST.get('Doctor')
        dept=request.POST.get('department')
        date=request.POST.get('Date')
        time=request.POST.get('Time')
        gender=request.POST.get('gender')
        
        if Booking.objects.filter(Phone=phone).exists():
            return JsonResponse({'error':"your are aleady booked"})
        else:
           
            last_token=Booking.objects.all().order_by('Token').last()
            new_token=last_token.Token+1

            Booking.objects.create(Name=name,Age=age,DOB=dob,Phone=phone,Address=address,Email=email,
                               Appointment_Doctor=doctor,Appointment_dept=dept,Appointment_Date=date,
                               Appointment_Time=time,Gender=gender,Token=new_token)  
            return HttpResponse(f"your booking successfully, Token number is {new_token}")
    else:
      return JsonResponse({'error':'The method is wrong'})




























@csrf_exempt
def data_of_Doctors(request):
   if request.method=="POST":
      Name = request.POST.get('name')
      User_name=request.POST.get('username')
      Email = request.POST.get('email')
      Category=request.POST.get('category')
      Phone_number = request.POST.get('phone')
      Age = request.POST.get('age')
      Gender = request.POST.get('gender')
      
      if Doctors.objects.filter(USER_NAME=User_name).exists():
          data=Doctors.objects.get(USER_NAME=User_name)
          datas=Registrationform.objects.get(USER_NAME=User_name)
          datas.EMAIL=data.EMAIL=Email
          data.NAME=datas.NAME=Name
          data.CATEGORY=Category
          data.PHONE_NUMBER=Phone_number
          data.AGE=Age
          data.GENDER=Gender
          data.save()
          datas.save()

          return JsonResponse({'success':'data entry successfully'})
      else:
            return JsonResponse({'error':'user not found , try after Registration'})
    
   else:
        return JsonResponse({'error':'method is wrong'})
@csrf_exempt
def data_of_Staffs(request):
   if request.method=="POST":
      Name = request.POST.get('name')
      User_name=request.POST.get('username')
      Email = request.POST.get('email')
      Category=request.POST.get('category')
      Phone_number = request.POST.get('phone')
      Age = request.POST.get('age')
      Gender = request.POST.get('gender')
      
      if Staffs.objects.filter(USER_NAME=User_name).exists():
          data=Staffs.objects.get(USER_NAME=User_name)
          datas=Registrationform.objects.get(USER_NAME=User_name)
          datas.EMAIL=data.EMAIL=Email
          data.NAME=datas.NAME=Name
          data.CATEGORY=Category
          data.PHONE_NUMBER=Phone_number
          data.AGE=Age
          data.GENDER=Gender
          data.save()
          datas.save()

          return JsonResponse({'success':'data entry successfully'})
      else:
            return JsonResponse({'error':'user not found , try after Registration'})
    
   else:
        return JsonResponse({'error':'method is failed'})
@csrf_exempt
def data_of_Patients(request):
   if request.method=="POST":
      Name = request.POST.get('name')
      User_name=request.POST.get('username')
      Email = request.POST.get('email')
      Category=request.POST.get('category')
      Phone_number = request.POST.get('phone')
      Age = request.POST.get('age')
      Gender = request.POST.get('gender')
      
      if Patients.objects.filter(USER_NAME=User_name).exists():
          data=Patients.objects.get(USER_NAME=User_name)
          datas=Registrationform.objects.get(USER_NAME=User_name)
          datas.EMAIL=data.EMAIL=Email
          data.NAME=datas.NAME=Name
          data.CATEGORY=Category
          data.PHONE_NUMBER=Phone_number
          data.AGE=Age
          data.GENDER=Gender
          data.save()
          datas.save()

          return JsonResponse({'success':'data entry successfully'})
      else:
            return JsonResponse({'error':'user not found , try after Registration'})
    
   else:
        return JsonResponse({'error':'data entry failed'})
                