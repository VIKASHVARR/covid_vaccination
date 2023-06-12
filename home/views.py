from django.shortcuts import render,redirect
import random
from django.core.mail import send_mail
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.hashers import make_password
from .models import district,centers,list

def home(request):
    return render(request,"home.html")

def signin(request):
    return render(request,"signin.html")

def signin_verification(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        request.session["username"]=username
        request.session["password"]=password1
        request.session["email"]=email
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('signin')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('signin')
            else:
                send_otp(request)
                return render(request,'otp.html',{"email":email})
        else:
            messages.info(request,"password mismatch")
            return redirect("signin")


def send_otp(request):
    s=""
    for x in range(0,4):
        s+=str(random.randint(0,9))
    request.session["otp"]=s
    send_mail("otp for sign up",s,'djangoalerts0011@gmail.com',[request.session['email']],fail_silently=False)
    return render(request,"otp.html")

def  otp_verification(request):
    if  request.method=='POST':
        otp_=request.POST.get("otp")
    if otp_ == request.session["otp"]:
        encryptedpassword=make_password(request.session['password'])
        nameuser=User(username=request.session['username'],email=request.session['email'],password=encryptedpassword)
        nameuser.save()
        messages.info(request,'signed in successfully...')
        User.is_active=True
        return redirect('home')
    else:
        messages.error(request,"otp doesn't match")
        return render(request,'otp.html')

def user_login(request):
    return render(request,"login.html")

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
            return redirect("user_login")
        
def district_views(request):
    try:
        request.session['user']
        dests=district.objects.all()
        return render(request,"cities.html",{"dests":dests})
    except:
        messages.info(request,"log in plz")
        return render(request,"home.html")
    

def center(request):
      dest=request.GET.get('place')
      display=centers.objects.filter(city_id=dest)
      return render(request,'centers.html',{'display':display})
  
def logout(request):
    try:
        del request.session['user']
        auth.logout(request)
        messages.info(request,"logged out successfully")
        return render(request,'home.html')
    except:
        messages.error(request,"no account is logged in")
        return render(request,"home.html")
  
def booking(request):
    place=request.GET.get('place')
    obj=centers.objects.filter(id=place).values()
    if list.objects.filter(name=request.session['user']).exists():
        messages.info(request,"slot already booked for the user...book after 90 days")
        return redirect("home")
    if obj[0]["dose_avva"]==0:
        messages.info(request,"sorry,all slots has been filled")
    else:
        print(obj)
        vacciner=list(name=request.session['user'],vaccine=obj[0]['vaccine'],area=obj[0]["center_name"])
        vacciner.save()
        b=(obj[0]["dose_avva"]) 
        a=b-1
        obj.update(dose_avva=a)
        messages.info(request,"your vaccination has been scheduled")
    return redirect('home')


        
