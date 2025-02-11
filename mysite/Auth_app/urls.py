from django.urls import path,include
from . import views

urlpatterns = [
    path('hello/',views.print_hello),
    path('home/',views.home),
    path('all-data/',views.all_data)
]
