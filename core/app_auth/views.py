from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from.forms import LoginForm,RegisterForm
from django.contrib import messages
"""
def login_blog(request):
    if request.method=="POST":
        username=request.POST['username']
        pwd=request.POST['pwd']
        user =authenticate(username=username,password=pwd)
        if user is not None:
            return redirect("home")
        else:
            return render(request,"login.html")   
    return render(request,"login.html") 
    """

def login_blog(request):
    if request.method=="POST":
        form=LoginForm(request.POST) 
        if form.is_valid():
            username=form.cleaned_data['username']
            pwd=form.cleaned_data['pwd']
            user=authenticate(username=username,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Authentification échouée")
                return render(request,'login.html',{"form":form})   
        
        else:
            return render(request,'login.html',{"form":form})
    else:
        form=LoginForm()
        return render(request,'login.html',{"form":form})    


def register(request):
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pwd=form.cleaned_data['pwd']
            user=User.objects.create_user(username=username,password=pwd)
            if user is not None:
                return redirect('login-blog')
            else:
                return render(request,'register.html',{'form':form})    
        else:
            return render(request,'register.html',{'form':form})

        return render(request,'register.html',{})



    form=RegisterForm()
    return render(request,'register.html',{'form':form})



def deconnecter(request):
    logout(request)
    return redirect('home')

      

