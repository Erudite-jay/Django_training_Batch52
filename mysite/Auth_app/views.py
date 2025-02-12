from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Auth_app.models import Contact
from .serializers import ContactSerializer
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def print_hello(request):
    return HttpResponse("Hello World !")

def home(request):
    return render(request,'Auth_app/index.html')

@csrf_exempt
def all_data(request):
    if request.method == 'GET':  #if request is a GET request
        contacts = Contact.objects.all() #queryset
        serializer = ContactSerializer(contacts, many=True) #serialized data ==~json format
        return JsonResponse(serializer.data,safe=False)
    
    if request.method == 'POST': 
        try:
            input_data=json.loads(request.body) #json format
            serializer=ContactSerializer(data=input_data)

            if serializer.is_valid():
                serializer.save()  # if my serializer is connected to DB == modelserializer

                #normal serializer
                # data=serializer.data
                # record=Contact.objects.create(
                #     fullname=data.get('fullname'),
                #     email=data.get('email'),
                #     phone=data.get('phone'),
                #     messsage=data.get('messsage')
                #     )
                # record.save() 
            
                return JsonResponse(
                    {
                        "message": "Data created successfully",
                        "data": serializer.data
                    },
                    status=201,
                )
            else: #serial
                return JsonResponse(
                    {
                        "error": serializer.errors
                    },
                    status=400,
                )
        except Exception as e:
            return JsonResponse(
                {
                    "error": str(e)
                },
                status=400,
            )
        

@csrf_exempt
def single_user_data(request, pk):
    if request.method == 'GET':  #if request is a GET request
      try:
          user=Contact.objects.get(pk=pk) #object
          serializer=ContactSerializer(user) #serialized data ==~json format
          return JsonResponse({
              "data": serializer.data
          },status=200)
      except Contact.DoesNotExist:
          return JsonResponse({
              "error": "User not found"
          },status=404)
      except Exception as e:
          return JsonResponse({
              "error": str(e)
          },status=400)
    
    if request.method == 'PUT': #if request is a PUT request
        try:
            user=Contact.objects.get(pk=pk) #object
            input_data=json.loads(request.body) #json format
            serializer=ContactSerializer(user, data=input_data) 

            if serializer.is_valid():
                serializer.save()  # if my serializer is connected to DB == modelserializer
                return JsonResponse({
                    "message": "Data updated successfully",
                    "data": serializer.data
                },status=200)
            else: #serial
                return JsonResponse({
                    "error": serializer.errors
                },status=400)
        except Contact.DoesNotExist:
            return JsonResponse({
                "error": "User not found"
            },status=404)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=400)
        
    if request.method == 'DELETE': #if request is a DELETE request
        try:
            user=Contact.objects.get(pk=pk) #object
            user.delete() #delete from DB
            return JsonResponse({
                "message": "User deleted successfully"
            },status=204)
        except Contact.DoesNotExist:
            return JsonResponse({
                "error": "User not found"
            },status=404)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=400)