from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def loginView(request):
    if request.method=="POST":
        usern=request.POST.get('lion')
        passw=request.POST.get('goat')
        c=authenticate(request,username=usern,password=passw)
        if c is not None:
            login(request,c)
            #request.session['college']="SRIT-ATP"
            if c.is_staff:
                return redirect('')

        #(check.first_name)
    return render(request,'login.html')

def homeView(request):
    #a=request.session['college']
    return render(request,'index.html')

def aboutView(request):
    return render(request,'about.html')

def contactView(request):
    return render(request,'contact.html')

def usersView(request):
    result=User.objects.all()
    return render(request,'users.html',{'res':result})

@login_required(login_url="loginPage")
def postsView(request):
    return render(request,'posts.html')


def logoutView(request):
    logout(request)
    return redirect('homePage')