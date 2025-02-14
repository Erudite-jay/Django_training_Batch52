from django.contrib.auth.models import User # sender
from django.contrib.auth.signals import user_logged_in # signal

from django.db.models.signals import pre_save
from django.dispatch import receiver





#reciever
def login_success(sender,request,user,**kwargs):
    print("I am user logged in signal -> reciever function")
    print("sender: " ,sender)
    print("request: ",request)
    print("user: ", user)
    print("email: ",user.email)
    print("kwargs: ",kwargs)


#write a logic to send email to user   -> that you have loggef in successful
#connect signal
user_logged_in.connect(login_success,sender=User)




@receiver(pre_save, sender=User)
def save_begin(sender,**kwargs):
    print("I am pre_save signal -> reciever function")
    print("sender: " ,sender)
    print("kwargs: ", kwargs)

    #write the logic to send email to user for the confirmation -> 