from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chaithu(request):
    return render(request,'chaithu.html')
def divya(request):
    return render(request,'divya.html')
def string(request):
    return HttpResponse('<h1>This is string as a response</h1>')