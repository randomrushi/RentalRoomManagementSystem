from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from .models import Tenent,Owner,Property

# Create your views here.
def home(request) :
    featured_prop = Property.objects.filter()
    return render(request,'index.html',{'props' : featured_prop})

def profile(request) :
    return 

def aboutus(request) :
    return render(request,'about_us.html')

def owner(request):
    return render(request,'owner.html')

def tenant(request):
    return render(request,'tenant.html')

def login(request) :
    return render(request,'login.html')

def login_tenant(request) :
    return render(request,'login.html')

def tenant_profile(request) :
    return render(request,'profile_tenant.html')

def owner_profile(request) :
    return render(request,'profile_owner.html')

def register_tenant(request) :
    if request.method == "POST" :
        first_name  = request.POST["first_name"]
        last_name   = request.POST["last_name"]
        email       = request.POST["email"]
        password1   = request.POST["password1"]
        password2   = request.POST["password2"]

        tenent = Tenent(first_name = first_name , last_name = last_name , email = email ,password = password1 )
        tenent.save()
        return render(request,'home.html')
    else :
        return render(request,'home.html')

def register_owner(request) :
    if request.method == "POST" :
        first_name  = request.POST["first_name"]
        last_name   = request.POST["last_name"]
        email       = request.POST["email"]
        password1   = request.POST["password1"]
        password2   = request.POST["password2"]

        owner = Owner(first_name = first_name , last_name = last_name , email = email ,password = password1 )
        owner.save()
        return render(request,'home.html')
    else :
        return render(request,'home.html')
