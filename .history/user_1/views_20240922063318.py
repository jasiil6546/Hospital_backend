from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse,HttpResponse
from user_1.serializer import RegisterSerializer
from .models import Registrationform
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
                if Category =="Doctor"
                
            # data=Registrationform.objects.create(NAME=Name,PASSWORD=make_password(Password),EMAIL=Email,PHONE_NUMBER=Phone_number,CATEGORY=Category,AGE=Age,GENDER=Gender)
            # serializer=RegisterSerializer(data)
            # return JsonResponse({'status':'sucess','data':serializer.data},status=201)
    else:  
           return HttpResponse("no data")
def login(request):
    Name= request.post.get('name')
    Password = request.post.get('password')                       
    data=Registrationform.objects.create(NAME=Name,PASSWORD=make_password(Password),)
    data.save()
    return HttpResponse(login)