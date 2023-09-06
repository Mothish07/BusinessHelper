from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.
#Index Page Call function
def home(request):
    return render(request,'Authentication/index.html')
#Login Page Calling function
def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        user = authenticate(username=username , password=passwd)
        
        if user is not None:
            login(request,user)
            fname = user.first_name
            lname = user.last_name
            emailId = user.email
            client = user.username
            dateupdate = date.today()
            return render(request,'Authentication/profileinfo.html',{'fname':fname,'date':dateupdate, 'lname':lname, 'username':client, 'email':emailId})
        else:
            messages.error(request,"Please Enter correct Credentials")
            return redirect('home')
        
    return render(request,'Authentication/index.html')
#Create Page Call function
def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email =request.POST['email']
        passwd = request.POST['passwd']
        cpasswd = request.POST['cpasswd']
        
        if User.objects.filter(username=username):
            messages.error(request,"Username already exists ! please try some other username")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already registered ! please try some other email id ")
            return redirect('signup')
        if len(username)>10:
            messages.error(request,'Username under 10 Character')
            return redirect('signup')
        if passwd != cpasswd:
            messages.error(request,'Password and Confirm Password mismatched')
            return redirect('signup')
        if not username.isalnum():
            messages.error(request,'UserName must be alpha numeric')
            return redirect('signup')
    
            
        
        myuser = User.objects.create_user(username,email,passwd)
        myuser.first_name = fname
        myuser.last_name =lname
        myuser.save()
        
        messages.success(request,"Your Account Has Been Created Successfully ! ")
        return render(request,'Authentication/index.html')
      
    return render(request,'Authentication/signup.html')


def signout(request):
    logout(request)
    messages.success(request,'Logged out Successfully !')
    return redirect('home') 

        
        
