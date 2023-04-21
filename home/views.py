from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import Indianspots,Foreignspots,Travel

  
def home(request):
    try:
       name=request.session['user']
    except:
        name="login"
    return render(request,"home.html",{"name":name})

def india(request):
    try:
        request.session['user']
        dests=Indianspots.objects.all()
        return render(request,"index1.html",{"dests":dests})
    except:
        messages.error(request,"login to continue")
        return render(request,'home.html')

def foreign(request):
    try:
        request.session['user']
        dests=Foreignspots.objects.all()
        return render(request,"index2.html",{"dests":dests})
    except:
        messages.error(request,"login to continue")
        return render(request,'home.html')
    
def signin(request):
    return render(request,"signin.html")

def login(request):
    return render(request,"login.html")

def signin_verification(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        request.session["username"]=username
        request.session["password"]=password
        request.session["email"]=email
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('signin')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('signin')
            else:
                send_otp(request)
                return render(request,'otp.html')
        else:
            messages.info(request,"password mismatch")
            return redirect("signin")
    
def send_otp(request):
    s=""
    for x in range(0,4):
        s+=str(random.randint(0,9))
    request.session["otp"]=s
    send_mail("otp for sign up",s,'djangoalerts0011@gmail.com',[request.session['email']],fail_silently=True,)
    return render(request,"otp.html")


def otp(request):
    if  request.method=='POST':
        otp_=request.POST.get("otp_by_user")
    if otp_ == request.session["otp"]:
        encryptedpassword=make_password(request.session['password'])
        nameuser=User(username=request.session['username'],email=request.session['email'],password=encryptedpassword)
        nameuser.save()
        messages.info('signed in successfully...')
        User.is_active=True
        return redirect('home')
    else:
        messages.error(request,"otp doesn't match")
        return render(request,'otp.html')

def verify(request):
     if request.method=="POST":
        name=request.POST["username"]
        password=request.POST["password"]
        encryptedpassword=make_password(request.POST['password'])
        nameuser=auth.authenticate(username=name,password=password)
        if nameuser is not None:
            request.session['user']=nameuser.username
            return render(request,"home.html",{'name':request.session['user']})
        else:
            messages.info(request,"invalid login")
            return redirect("login")
        
def logout(request):
    try:
        del request.session['user']
        auth.logout(request)
        messages.info(request,"logged out successfully")
        return render(request,'home.html')
    except:
        messages.error(request,"no account is logged in")
        return render(request,"home.html")
    
def user(request):
    display=User.objects.get(username =request.session['user'])
    user=Travel.objects.filter(name =request.session['user'])
    return render(request,"user.html",{"detail":display,"user":user})

def booking(request):
    place=request.GET.get('place')
    display=Indianspots.objects.filter(name=place)
    return render(request,'booking.html',{'display':display})

def fbooking(request):
    place=request.GET.get('place')
    display=Foreignspots.objects.filter(name=place)
    return render(request,'booking.html',{'display':display})

def contact(request):
    return render(request,"contact.html")

def aboutus(request):
    return render(request,"about.html")

def success(request):
    messages.info("tickets booked successfully")
    return render(request,"home.html")

def failure(request):
    messages.error("payment error")
    return redirect('payment')

def payment(request):
    pass