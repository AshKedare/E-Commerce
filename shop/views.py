from django.shortcuts import redirect, render
from django.http import HttpResponse
from shop.models import Product, Contact
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import json
from django.contrib import messages


# Create your views here.


def index(request): 
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1,nslides), nslides])
    # params = {'no_of_slides':nslides, 'range':range(1, nslides), 'product':products}
    # allprods = [[products, range(1, nslides), nslides], 
    #             [products, range(1, nslides), nslides]]
    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, "shop/about.html")

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        issue = request.POST.get('issue','')
        query = request.POST.get('query','')
        contact = Contact(name=name, email=email, phone=phone, issue=issue, query=query)
        contact.save()
    return render(request, "shop/contact.html")

def tracker(request):
    return render(request, "shop/tracker.html")

def search(request):
    return render(request, "shop/search.html")

def product(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request, "shop/product.html", {'product':product[0]})

def checkout(request):
    product = Product.objects.filter()
    return render(request, "shop/checkout.html",{'product':product})

def authenticated(request):
    return render(request, 'shop/authenticated.html')

def user_login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        # if the user is authenticated
        if user is not None:
            login(request,user)
            request.session['is_logged_in'] = True
            return redirect('index')
        else:
            messages.error(request, "Please enter valid Credentials")
            return redirect('user_login')
    is_logged_in = request.session.get('is_logged_in', False)
    return render(request, 'shop/login.html')

from django.db import IntegrityError

def signup(request):
    if request.method == 'POST':
        # Extract user input
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, 'shop/signup.html', {'name': name, 'email': email, 'phone': phone})
        
        try:
            # Attempt to create user
            myuser = User.objects.create_user(name, email, pass1)
            myuser.phone = phone
            myuser.save()
            
            messages.success(request, "Your account has been created successfully")
            return redirect('user_login')  # Redirect to login page after successful signup
        except IntegrityError:
            messages.error(request, "Username or email is already taken. Please log in instead.")
            return redirect('user_login')  # Redirect to login page if user already exists

    return render(request, 'shop/signup.html')

def logout(request):
    return render()