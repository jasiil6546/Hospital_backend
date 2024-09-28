from django.shortcuts import render

# Create your views here.
@csrf_exempt
def Registration(request):
    if request.method == 'POST':
            Name = request.POST.get('name')
            Password = request.POST.get('password')
            Email = request.POST.get('email')
            #Category=request.post.get('category')
            Phone_number = request.POST.get('phone')
            Age = request.POST.get('age')
            Gender = request.POST.get('gender')
            
        
            data=Registrationform.ojects.create(NAME=Name,PASSWORD=make_password(Password),EMAIL=Email,PHONE_NUMBER=Phone_number,AGE=Age,GENDER=Gender)
            serializer=RegisterSerializer(data)
            return JsonResponse({'status':'sucess','data':serializer.data},status=201)
    else:  
           return HttpResponse("no data")