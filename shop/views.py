import json
from django.http import HttpResponse , JsonResponse
from django.shortcuts import redirect, render

from shop.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    products = Product.objects.filter(trending=1)
    return render(request, "shop/index.html",{"products":products})


def logout_page(request):
   if request.user.is_authenticated:
      logout(request)
      messages.success(request,"Logged out Successfully")
   return redirect("/")   

def login_page(request):
   if request.user.is_authenticated:
      return redirect('/')
   else:
      if request.method=='POST':
         name=request.POST.get('username')
         pwd=request.POST.get('password')
         User=authenticate(request,username=name,password=pwd)
         if User is not None:
            login(request,User)
            messages.success(request,"Logged in Successfully")
            return redirect("/")
         else:
            messages.error(request,"Invalid User Name or Password")
            return redirect("/login")
      return render(request,"shop/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
       form=CustomUserForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request, "Registration Success You can Login Now...!")
          return redirect('/login')
    return render(request, "shop/register.html",{'form':form})

def collections(request):
    category = Catagory.objects.filter(status=0)  # Fixed variable name
    return render(request, "shop/collections.html",{"category": category})  # Fixed variable name

def collectionsview(request,name):
  if(Catagory.objects.filter(name=name,status=0)):
    products=Product.objects.filter(catagory__name=name)
    return render(request, "shop/products/index.html",{"products": products,"catagory_name":name}) 
  else:
    messages.warning(request,"No Such Catagory Found")
    return redirect('collections')
  
def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
       if(Product.objects.filter(name=pname,status=0)):
          products=Product.objects.filter(name=pname,status=0).first()
          return render(request,"shop/products/product_details.html",{"products":products})
       else:
          messages.error(request,"No Such Catagory Found") 
          return redirect('collections')
    else:
       messages.error(request,"No Such Catagory Found") 
       return redirect('collections') 