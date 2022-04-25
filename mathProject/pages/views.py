



from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse 
from users.models import Student,Login,User
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

def existStudentByEmail(mail,password):
    students = Student.objects.all()

    for student in students:
        if student.email.lower() == mail.lower() and student.check_password(password) :
            print('account found by email')
            return True

    return False

def existStudentByCode(code,password):

    try:
        
        student = get_object_or_404(Student,id=code)
        print(student)
        print(password)
        if student and student.check_password(password) :
            print('account found by code')
            return True
    except:
        return False

    return False


def loginPage(request):
    if request.method == "POST":

        mail = request.POST['email']
        password = request.POST.get('password')

        print(mail)
        print(password)
        
        if existStudentByEmail(mail,password):
            
            try:
                #student = get_object_or_404(Student,email=mail.lower())
                
                student = authenticate(request,username=mail.lower(),password=password)
                print(student)
                if student == None:
                    return render(request, 'pages/signin.html', {

                    "errorMessage": "No Such Student is created"
                })

                loginObject = Login(user=student,email=mail)
                loginObject.save()
                print(loginObject)
                login(request,student)

                return redirect(reverse("dashboard"))
                
            except:
                return render(request, 'pages/signin.html', {
                    "errorMessage": "An Error Occured ... Try Again Later"
                })
           
        elif existStudentByCode(mail,password):

            try:
                user = get_object_or_404(User,id=mail)

                student = authenticate(request,username=user.email.lower(),password=password)
                #print(student)
                if student == None:
                    return render(request, 'pages/signin.html', {

                    "errorMessage": "No Such Student is created"
                })


                loginObject = Login(user=student,email=student.email)
                loginObject.save()

                login(request,student)

                return redirect(reverse("dashboard"))
                
            except:
                return render(request, 'pages/signin.html', {
                    "errorMessage": "An Error Occured ... Try Again Later"
                })
           
        else:

            return render(request, 'pages/signin.html', {
                "errorMessage": "Email or Code or password or both are  incorrect "
            })
            

        
    return render(request,'pages/signin.html')


def signupPage(request):
    levels=Level.objects.all()

    if request.method == "POST":

        fname = request.POST['f-name']
        lname = request.POST['l-name']
        Pass = request.POST.get('password')
        Pass2 = request.POST.get('confirmPassword')
        mail = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        parentphone = request.POST.get('parentPhone')
        level = request.POST.get('level')
        schoolName  = request.POST.get('school-name')
        address = request.POST.get('address')

        
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
                username=fname+" "+lname,
                last_name=lname,
                first_name=fname,
                email=mail.lower(),
                #password=Pass,
                phone=phone,
                gender=gender,
                parentPhone=parentphone,
                level=levelObject,
                address=address,
                schoolname=schoolName
            )
            student.set_password(Pass)
            
            student.save()
            

            messages.success(request,"User is created successfully")
            print("Success")
            return render(request,'pages/signUp.html',{
                "levels":levels,
                "message":"User is created successfully ",
                "code":student.id,
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