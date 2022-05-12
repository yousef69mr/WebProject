
import threading
from django.http import  JsonResponse
from django.shortcuts import get_object_or_404 , render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def getUsers(request):
    users = User.objects.all()
    return JsonResponse({
        "students":list(users.values())
    })

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()



def send_activation_email(user,request):

    
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    print(current_site)
    print(email_subject)
    print(urlsafe_base64_encode(force_bytes(user.id)))
    email_body = render_to_string('users/activate.html',{
        'user' : user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token':generate_token.make_token(user),
    })
    
    print(email_body)
    print(user.email)
    print(settings.EMAIL_FROM_USER)
    print(settings.EMAIL_HOST_PASSWORD)

    email_message = EmailMessage(subject=email_subject,body=email_body,
        from_email= settings.EMAIL_FROM_USER,
        to=[user.email],
        )


    EmailThread(email_message).start()

    
    

def activate_user(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User,id=uid)
        print(uid)
        print(user.email)
    except Exception as e :
        user = None

    if user and generate_token.check_token(user,token):
        user.is_verified =True
        #user.is_active =True

        user.save()
        print("activate_user")
        return render(request,'pages/signin.html',{
            
            "message":"User is verified successfully .. You can login NOW  :)",
            "code":user.id,
            "alertType":"alert-success",

        })

    return render(request,'users/activate-fail.html')