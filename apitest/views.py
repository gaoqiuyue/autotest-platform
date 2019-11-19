from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse("hello test")  #返回 HttpResponse 响应函数