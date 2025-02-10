from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    return HttpResponse("Hello World !")

def home(request):
    return render(request,'Auth_app/index.html')