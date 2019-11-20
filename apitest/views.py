from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse("hello test")  #返回 HttpResponse 响应函数
def login(request):
    if request.POST:
        username=password=""
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user']=username
            response=HttpResponseRedirect("/index/")
            return  response
        else:
            return render(request,'login.html',{"error":"username or password error"})

    return render(request,'login.html')
def home(request):
    return render(request,"home.html")
def index(request):
    return render(request,"index.html")