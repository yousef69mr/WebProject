
import threading
from django.http import  JsonResponse
from django.shortcuts import get_object_or_404 , render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.views import View
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.


def getDataOfGender(request):
    if request.is_ajax:

        users = User.objects.all()
        male = users.filter(gender = 'male').count()
        female = users.filter(gender = 'female').count()

        
        print(male)
        print(female)

        return [female,male]
    
    
    
    
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
        self.email.send(fail_silently=False)

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

    return render(request,'users/fail.html')



def send_reset_password_email(request,user):

    
    current_site = get_current_site(request)
    email_subject = 'Reset Password your account'
       
    print(current_site)
    print(email_subject)
    
    print(urlsafe_base64_encode(force_bytes(user.id)))
    email_contents = render_to_string('users/reset-user-password.html',{
        'user' : user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token':generate_token.make_token(user),
    })
    
    print(email_contents)
    print(user.email)
    print(settings.EMAIL_FROM_USER)
    print(settings.EMAIL_HOST_PASSWORD)
    
    email_message = EmailMessage(subject=email_subject,body=email_contents,
        from_email= settings.EMAIL_FROM_USER,
        to=[user.email],
        )


    EmailThread(email_message).start()





    

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

class RequestPasswordResetEmail(View):
    def get(self,request):
        return render(request,'users/reset-password.html')

    def post(self,request):
        email = request.POST.get('email')

        
        if not validateEmail(email):
            return render(request,'users/reset-password.html',{
            
                "message":"Please Enter a valid Email",
                "alertType":"alert-danger",
                

            })

        try:
            print(email.lower())
            user = User.objects.get(email=email.lower()) 

            send_reset_password_email(request,user)

            return render(request,'users/reset-password.html',{
            
                "message":"Confirmation Email sent to you ,Please check your email Inbox",
                "alertType":"alert-success",
               

            })

        except:
            return render(request,'users/reset-password.html',{
            
                "message":"No such a User with this Email",
                "alertType":"alert-danger",
                "values":request.POST,

            })

        


class CompletePasswordReset(View):
    def get(self,request,uidb64,token):
        print("there")
        print(uidb64,token)

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(User,id=uid)
            print(uid)
            print(user.email)
            return render(request,'users/set-new-password.html',{
                'uidb64':uidb64,
                'token':token,
                'user':user,
            })

        except Exception as e :
            user = None



        return render(request,'users/set-new-password.html',{
            'user':user,
        })

    def post(self,request,uidb64,token):
        if request.method == 'POST':
            email = request.POST.get('email')

            try:
                
                user = get_object_or_404(User,email=email.lower())
                
                print(user)
                print(user.email)
            except:
                user = None
                
            if user :
                
                Pass = request.POST.get('password')
                Pass2 = request.POST.get('confirmPassword')
                print(Pass)

                if Pass != Pass2 :
                    return render(request, 'users/set-new-password.html', {
                        "message":"Two Passwords don't match",
                        "alertType":"alert-danger",
                        'user':user,

                    })

                try:
                    print("changed")
                    user.set_visible_password(Pass)
                    user.set_password(Pass)
                    user.save()

                    return render(request, 'pages/signin.html', {
                            "message":"Password changed successfully",
                            "alertType":"alert-success",
                        
                        })

                except:
                    return render(request, 'users/set-new-password.html', {
                            "message":"An Error occured",
                            "alertType":"alert-danger",
                        
                        })

            
        return render(request,'users/fail.html')



def set_new_password(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User,id=uid)
        print(uid)
        print(user.email)
        

    except Exception as e :
        user = None

    if user and generate_token.check_token(user,token):
        
        #user.is_active =True
        print("method")
        if request.method == "POST":
            print("here")
            Pass = request.POST.get('password')
            Pass2 = request.POST.get('confirmPassword')
            print(Pass)

            if Pass != Pass2 :
                return render(request, 'users/set-new-password.html', {
                    "message":"Two Passwords don't match",
                    "alertType":"alert-danger",
                    'user':user,
                    'uidb64':uidb64,
                    'token':token,

                })

            try:
                
                user.set_visible_password(Pass)
                print(user.raw_password)
                user.set_password(Pass)
                print(user.password)
                user.save()

                print("changed")
                
                return render(request, 'pages/signin.html', {
                        "message":"Password changed successfully",
                        "alertType":"alert-success",
                    
                    })

            except:
                print(token,uidb64)
                return render(request, 'users/set-new-password.html', {
                        "message":"An Error occured",
                        "alertType":"alert-danger",
                        'user':user,
                        'uidb64':uidb64,
                        'token':token,
                    
                })

        return render(request,'users/set-new-password.html',{
            'user':user,
            'uidb64':uidb64,
            'token':token,
        })

    
    return render(request,'users/fail.html')
