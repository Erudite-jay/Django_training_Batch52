from .models import Contact
from rest_framework import serializers

#simple serialization
class ContactSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=40)
    phone=serializers.CharField(max_length=10)
    messsage=serializers.CharField(max_length=250)
