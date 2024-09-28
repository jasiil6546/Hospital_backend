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
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone_number = request.POST.get('phone_number')
        Dob = request.POST.get('dob')
        Age = request.POST.get('age')
        Gender = request.POST.get('gender')
        
        
        if Booking.objects.filter(PHONE_NUMBER=Phone_number).exists():
            return JsonResponse({'error': "You are already booked."})
        
        
        last_booking = Booking.objects.all().order_by('Token').last()
        if last_booking:
            new_token = last_booking.Token + 1
        else:
            new_token = 1  
        
        
        Booking.objects.create(
            NAME=Name,
            AGE=Age,
            DOB=Dob,
            PHONE_NUMBER=Phone_number,
            EMAIL=Email,
            GENDER=Gender,
            Token=new_token
        )
        
        return HttpResponse(f"Your booking is successful. Token number is {new_token}")
    
    else:
        return JsonResponse({'error': "Booking failed"})

@csrf_exempt
def deletebooking(request): 
    Phone_number = request.POST.get('phone')

    try:
        
        booking = Booking.objects.get(PHONE_NUMBER=Phone_number)
        booking.delete()  
        return JsonResponse({'success': "The booking has been deleted"})
    except Booking.DoesNotExist:
        return JsonResponse({'error': "No booking found for this phone number"})

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
@csrf_exempt
def delete_data(request):
    if request.method == "POST":
        User_name = request.POST.get('username')
        try:
            registration = Registrationform.objects.get(USER_NAME=User_name)
            category = registration.CATEGORY

            
            if category == "Doctors":
                Doctors.objects.get(USER_NAME=User_name).delete()
                message = 'Deleted successfully data of doctors'
            elif category == 'Staffs':
                Staffs.objects.get(USER_NAME=User_name).delete()
                message = 'Deleted successfully data of staffs'
            else:
                Patients.objects.get(USER_NAME=User_name).delete()
                message = 'Deleted successfully data of patients'

        
            registration.delete()
            return JsonResponse({'status': message})

        except Registrationform.DoesNotExist:
            return JsonResponse({'error': 'User not found'})

    return JsonResponse({'error': 'Invalid request method'}) 
@csrf_exempt  
def diplay_details_of_doctors(request):
     
         Username=request.POST.get('username')
         
         if Doctors.objects.filter(USER_NAME=Username).exists():
             data=Doctors.objects.get(USER_NAME=Username)

             serializer=DoctorsSerializer(data)

             return JsonResponse({'status':'displayed','data':serializer.data})
           
         else:
             return JsonResponse({'error':'User unvailable'})
def display_staffs(request):
    Username=request.POST.get('username') 
    
    if Staffs.objects.filter(USER_NAME=Us)        