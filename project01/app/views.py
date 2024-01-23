from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'app/home.html')
    # data = render(request,'app/home.html')
    # data.set_cookie('name','Tarun')
    # data.set_cookie('age','37')
    # data.set_cookie('city','Bhopal')
    # return data

def about(request):
    return render(request,'app/about.html')

def service(request):
    return render(request,'app/service.html')

def content(request):
    return render(request,'app/content.html')

def register(request):
    return render(request,'app/register.html')

def login(request):
    return render(request,'app/login.html')

def savedata(request):
    name=request.POST['name']
    email=request.POST['email']
    contact=request.POST['contact']
    city=request.POST['city']
    password=request.POST['password']
    print(name)
    print(email)
    print(contact)
    print(city)
    print(password)
    response = render(request,'app/login.html')
    response.set_cookie('name',name)
    response.set_cookie('email',email)
    response.set_cookie('contact',contact)
    response.set_cookie('city',city)
    response.set_cookie('password',password)
    return response


def logindata (request):
    emailId = request.POST['email']
    password =request.POST['password']

    email_id = request.COOKIES['email']
    cooki_password = request.COOKIES['password']

    if email_id==emailId and password==cooki_password:
        name = request.COOKIES['name']
    
        return render (request,'app/dashboard.html',{"data":name})




