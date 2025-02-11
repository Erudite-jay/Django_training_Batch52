from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Auth_app.models import Contact
from .serializers import ContactSerializer
# Create your views here.

def print_hello(request):
    return HttpResponse("Hello World !")

def home(request):
    return render(request,'Auth_app/index.html')

def all_data(request):
        contacts = Contact.objects.all() #queryset
        serializer = ContactSerializer(contacts, many=True) #serialized data ==~json format
        return JsonResponse(serializer.data,safe=False)
