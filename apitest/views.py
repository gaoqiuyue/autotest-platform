from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from apitest.models import Apitest, Apistep, Apis


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

def logout(request):
    auth.logout(request)
    return render(request,'login.html')
@login_required
def apitest_manage(request):
    apitest_list=Apitest.objects.all()
    username=request.session.get("user","")
    return  render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list})
@login_required
def apistep_manage(request):
    apistep_list=Apistep.objects.all()
    username = request.session.get("user", "")
    return render(request, "apistep_manage.html", {"user": username, "apisteps": apistep_list})
@login_required
def apis_manage(request):
    api_list = Apis.objects.all()
    username = request.session.get("user", "")
    return render(request, "apis_manage.html", {"user": username, "apiss": api_list})

