
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse 
from users.models import Student,Login,User
from users.views import send_activation_email
from pages.models import Level,Message
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def index(request):

    levels= Level.objects.all()
    return render(request,'pages/index.html',{

        'levels':levels,

    })


def aboutPage(request):
    pass


def contactUsPage(request):
    if request.method == "POST":
        userName = request.POST['name']
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('message')

        print(userName)
        print(phone)
        print(email)
        print(subject)
        print(content)

        try:
            message = Message(sender=userName,email=email,phone=phone,message=content,subject=subject)
            message.save()

        except:
            return render(request, 'pages/contactFormPage.html', {
                "message": "An Error Occured ... Try Again Later"
            })


    return render(request,'pages/contactFormPage.html')


"""
def existEmail(mail):
    students = Student.objects.all()

    for student in students:
        if student.Email == mail.lower():
            print('email found')
            return True

    return False

def existPhone(phone):
    students = Student.objects.all()

    for student in students:
        if student.phone == phone:
            print('phone found')
            return True

    return False

"""
def existUserByUsername(username,password):
    try:
        user = User.objects.get(username= username)
        if user.check_password(password) :
            print('account found by Username')

            return True
        
    except:
        return False

    return False


def existUserByEmail(mail,password):
    try:
        user = User.objects.get(email= mail.lower())
        if user.check_password(password) :
            print('account found by email')

            return True
        
    except:
        return False

    return False

def existUserByCode(code,password):

    try:
        
        user = get_object_or_404(User,id=code)
        print(user)
        print(password)
        if user and user.check_password(password) :
            print('account found by code')
            return True
    except:
        return False

    return False


def loginPage(request):
    if request.method == "POST":

        input = request.POST.get('email')
        password = request.POST.get('password')

        print(input)
        print(password)
        #student = get_object_or_404(Student,email=mail.lower())
       
        if existUserByUsername(input,password):
            
            try:
                #student = get_object_or_404(Student,email=mail.lower())
                givenUser = get_object_or_404(User,username=input)
                
                if givenUser == None:

                    return render(request, 'pages/signin.html', {

                        "message":"No Such User is created",
                        "alertType":"alert-danger",

                    })

                
                user = authenticate(request,username=givenUser.email,password=password)
                print(user)
                if user == None:
                    return render(request, 'pages/signin.html', {

                    "message":"No Such User is created",
                    "alertType":"alert-danger",
                })

                if not user.is_active:
                    return render(request, 'pages/signin.html', {

                        "message": "This User is not activated ... please contact the Administrator",
                        "alertType":"alert-danger",
                    })


                if not user.is_verified:
                    return render(request, 'pages/signin.html', {

                        "message": "This User is not Verified ... please check your email inbox ",
                        "alertType":"alert-danger",
                    })

                loginObject = Login(user=user,email=user.email)
                
                loginObject.set_login_method('username')

                print("here")
                #loginObject.save()

                print(loginObject)
                login(request,user)

                return redirect(reverse("dashboard"))
                
            except:
                return render(request, 'pages/signin.html', {
                    "message": "An Error Occured ... Try Again Later",
                    "alertType":"alert-danger",
                })
           
        elif existUserByEmail(input,password):
            
            try:
                #student = get_object_or_404(Student,email=mail.lower())
                
                user = authenticate(request,username=input.lower(),password=password)
                print(user)
                if user == None:
                    return render(request, 'pages/signin.html', {

                    "message":"No Such User is created",
                    "alertType":"alert-danger",
                })

                if not user.is_active:
                    return render(request, 'pages/signin.html', {

                        "message": "This User is not activated ... please contact the Administrator",
                        "alertType":"alert-danger",
                    })


                if not user.is_verified:
                    return render(request, 'pages/signin.html', {

                        "message": "This User is not Verified ... please check your email inbox ",
                        "alertType":"alert-danger",
                    })

                loginObject = Login(user=user,email=user.email)
                
                loginObject.set_login_method('email')

                print("here")
                #loginObject.save()

                print(loginObject)
                login(request,user)

                return redirect(reverse("dashboard"))
                
            except:
                return render(request, 'pages/signin.html', {
                    "message": "An Error Occured ... Try Again Later",
                    "alertType":"alert-danger",
                })
           
        elif existUserByCode(input,password):

            try:
                givenUser = get_object_or_404(User,id=input)
                
                if givenUser == None:

                    return render(request, 'pages/signin.html', {

                        "message":"No Such User is created",
                        "alertType":"alert-danger",

                    })

                user = authenticate(request,username=givenUser.email,password=password)
                #print(student)
                if user == None:
                    return render(request, 'pages/signin.html', {

                    "message":"No Such User is created",
                    "alertType":"alert-danger",
                })

                if not user.is_verified:
                    return render(request, 'pages/signin.html', {

                        "message": "This User is not Verified ... please check your email inbox ",
                        "alertType":"alert-danger",
                    })

                loginObject = Login(user=user,email=user.email)
                loginObject.set_login_method('code')

                #loginObject.save()

                login(request,user)

                return redirect(reverse("dashboard"))
                
            except:
                return render(request, 'pages/signin.html', {
                    "message": "An Error Occured ... Try Again Later",
                    "alertType":"alert-danger",
                })
           
        else:

            return render(request, 'pages/signin.html', {
                "message": "Email or Code or password or both are  incorrect ",
                "alertType":"alert-danger",
            })
            

        
    return render(request,'pages/signin.html',{
        "message":"",
        "alertType":"",
    })


def signupPage(request):
    levels=Level.objects.all()

    if request.method == "POST":
        
        username = request.POST.get('username')
        fname = request.POST.get('f-name')
        lname = request.POST.get('l-name')
        Pass = request.POST.get('password')
        Pass2 = request.POST.get('confirmPassword')
        mail = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        parentphone = request.POST.get('parentPhone')
        level = request.POST.get('level')
        schoolName  = request.POST.get('school-name')
        address = request.POST.get('address')

        
        print(username)
        print(fname)
        print(lname)

        print(Pass)
        print(Pass2)
        print(mail)
        print(gender)
        print(phone)
        print(parentphone)
        print(level)
        print(schoolName)
        """
        if existPhone(phone):
            #message.append("This Phone Number is used before :( ")
            messages.warning(request,"This Phone Number is used before :( ")
            if not existEmail(mail):
                return redirect('signup')

        if existEmail(mail):
            #message.append("This Phone Number is used before :( ")
            messages.warning(request,"This Email is used before :( ")
            return redirect('signup')
            
        else:
        """
        try:

            levelObject = Level.objects.get(levelCode=level)
        
            #student = CustomAccountManager.create_student(request,mail,fname,lname,Pass,phone,parentphone,gender,levelObject,address,schoolName)
            
            student = Student(
                username=username,
                full_name=fname+" "+lname,
                last_name=lname,
                first_name=fname,
                email=mail.lower(),
                raw_password=Pass,
                phone=phone,
                gender=gender,
                parentPhone=parentphone,
                level=levelObject,
                address=address,
                schoolname=schoolName
            )
            student.set_password(Pass)
            
            student.save()

            #print("here")
            send_activation_email(student,request)
            #print("here")
            messages.success(request,"User is created successfully")
            print("Success")
            return render(request,'pages/signUp.html',{
                "levels":levels,
                "message":"User is created successfully But Not verified yet  :(",
                "subMessage":"So, Check your email inbox and click the Verification link .. Please  :)",
                "alertType":"alert-success",

            })
            #redirect("login")

        except:
            messages.warning(request,"An Error Occured during Registeration")
            return render(request, 'pages/signUp.html', {
                "levels":levels,
                "message":"An Error Occured during Registeration",
                "alertType":"alert-danger",

            })

    return render(request,'pages/signUp.html',{
        "levels":levels,
        "message":"",
        "alertType":"",
    })


def errorPage(request):
    return render(request,'pages/error.html')


def redirect_view(request):
    response = redirect('login')
    return response