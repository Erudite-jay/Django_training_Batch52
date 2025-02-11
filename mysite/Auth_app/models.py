from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=40)
    phone=models.CharField(max_length=10)
    messsage=models.TextField(max_length=250)