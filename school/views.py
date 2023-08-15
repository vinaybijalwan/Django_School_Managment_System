from django.shortcuts import render, redirect, HttpResponse
from school.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomerUser
from django.contrib.auth.decorators import login_required
# Create your views here.


def BASE(request):
    return render(request, 'base.html')

def Profile(request):
    user = CustomerUser.objects.get(id=request.user.id)
    #print(user)
    context = {
        "user":user,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def profile_update(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name =request.POST.get('fname')
        last_name =request.POST.get('lname')
        #email =request.POST.get('email')
        #username =request.POST.get('uname')
        password =request.POST.get('password')
        #print(profile_pic, first_name, last_name, password)
        try:
            Customeruser = CustomerUser.objects.get(id=request.user.id)
            Customeruser.first_name = first_name
            Customeruser.last_name = last_name
            #Customeruser.profile_pic = profile_pic 
            if password !=None and password != "":
                Customeruser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                Customeruser.profile_pic = profile_pic   
            Customeruser.save()
            messages.success(request, 'Your Profile Updated Sucessfully!')
            return redirect('profile')
        except:
            messages.error(request, 'Failed to Updated Profile')
    
                

    return render(request, 'profile.html')


def Login(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
                                         
        if user!=None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return HttpResponse('This is Staff Panel')
            elif user_type == '3':
                return HttpResponse('This is Student Panel')
            else:
                messages.error(request, 'Email & Password are Invalid')
                return redirect('login')
        else:
            messages.error(request, 'Email & Password are Invalid')
            return redirect('login')

        return None



def doLogout(request):
    logout(request)
    return redirect('login')