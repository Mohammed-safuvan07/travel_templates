from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method=='POST':
        user_name1 = request.POST['user_name']
        password1 = request.POST['password']
        user = auth.authenticate(username=user_name1,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid informations')
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        user_name = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        mails = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['c_password']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"username already Exit")
                return redirect('register')
            elif User.objects.filter(email=mails).exists():
                messages.info(request,'Email exists already')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,first_name=firstname,last_name=lastname,email=mails,password=password1)
                user.save();
                print('User Successfully Created')
                return redirect('login')

        else:
            print('Password is not match')
            return redirect('register')
        return redirect('/')
    return render(request,'info.html')