from django.http import JsonResponse
from django.shortcuts import render
from .models import User
# Create your views here.


def login_view(request):

    if request.session.get('username'):
        return JsonResponse({
            "message": "Already logged in",
            "user": request.session.get('username')
        },status=200)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user=User.objects.get(username=username)
            
            if user.password == password:
               request.session.set_expiry(10)
               request.session['username']=username
               return JsonResponse({
                   "message": "Login successful",
                   "user": user.username
               },status=200)
            
        except User.DoesNotExist:
            return JsonResponse({
                "error": "Invalid username or password"
            },status=401)
        
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)
        
    return render(request,'Session_app/login.html')