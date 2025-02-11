from django.contrib import admin
from .models import Contact

# Register your models here.

admin.site.register(Contact)

# @admin.register(Contact)
# class ContactTable(admin.ModelAdmin):
#     list_display=["id","fullname","email","phone","messsage"]