
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponseRedirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth import logout

from users.models import Student,User
from .models import File, Lecture,RegisteredLecture
from pages.models import Message,Level
# Create your views here.

def getFiles(request):
    files = File.objects.all()
    return JsonResponse({
        "files":list(files.values())
    })

def lecture(request,lecture_id):
    
    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        

    student = get_object_or_404(User,id=request.user.id)
    #print(request.user)
    
    lecture = get_object_or_404(Lecture,id=lecture_id)
    #print(lecture.id)
    #print(lecture.sourceLink)
    return render(request,'courses/lecture.html',{
        'student':student,
        "lecture":lecture,
        
    })

def lectures(request):

    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        

    student = get_object_or_404(User,id=request.user.id)
    registered = RegisteredLecture.objects.filter(user=student)
    lectures = registered.values_list('lecture',flat=True)
    #print(registered)
    #print(lectures)
    files = File.objects.all()
    
    if student.is_superuser :
        return render(request,'courses/lectures.html',{
        'student':student,
        'lectures':Lecture.objects.all(),
        'registeredLectures': lectures,
        'files':files,

        })

    return render(request,'courses/lectures.html',{
        'student':student,
        'lectures':Lecture.objects.filter(gradeLevel=student.level),
        'registeredLectures': lectures,
        'files':files,

    })

def regesteredlectures(request):

    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
    student = get_object_or_404(User,id=request.user.id)
    registered = RegisteredLecture.objects.filter(user=student)
    files = File.objects.all()
    print(registered)
    return render(request,'courses/registiredLectures.html',{
        'student':student,
        'registeredLectures': registered,
        'files':files,
    })


def dashboardPage(request):

    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
    student = get_object_or_404(User,id=request.user.id)
    
    return render(request,'courses/dashboard.html',{
        'student':student,
    })

def editProfilePage(request):

    levels=Level.objects.all()

    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
    student = get_object_or_404(User,id=request.user.id)

    if request.method == "POST":

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
        print(address)

        try:

            student.set_visible_password(Pass)
            student.set_password(Pass)
            
            student.save()

            #print("here")

            levelObject = Level.objects.get(levelCode=level)
            Student.objects.filter(id=request.user.id).update(
                username=fname+" "+lname,
                last_name=lname,
                first_name=fname,
                email=mail.lower(),
                #raw_password=Pass,
                phone=phone,
                gender=gender,
                parentPhone=parentphone,
                level=levelObject,
                address=address,
                schoolname=schoolName
            )

            print("I'm here")

            """
            student.set_first_name(fname)
            
            print(student.first_name)
            student.set_last_name(lname)
            print(student.last_name)
            student.set_username(student.first_name +" "+student.last_name)
            print(student.username)
            student.set_password(Pass)
            print(student.password)
            student.set_email(mail.lower())
            print(student.email)
            student.set_gender(gender)
            print(student.gender)
            student.set_Phone(phone)
            print(student.phone)
            student.set_Parent_Phone(parentphone)
            print(student.parentPhone)
            student.set_Educational_Level(levelObject)
            print(student.level)
            student.set_School_Name(schoolName)
            print(student.schoolname)
            student.set_Address(address)
            print(student.address)
            """

            return render(request,'courses/editProfile.html',{
            "levels":levels,
            "message":"User's Data is updated successfully ",
            "alertType":"alert-success",
            'student':student,
        })

        except:

            return render(request, 'courses/editProfile.html', {
                "levels":levels,
                "message":"An Error Occured during Registeration",
                "alertType":"alert-danger",
                'student':student,

            })
        

    return render(request,'courses/editProfile.html',{
        "levels":levels,
        "message":"",
        "alertType":"",
        'student':student,
    })



def contactUsPage(request):
     
    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
        
    student = get_object_or_404(Student,id=request.user.id)

    if request.method == "POST":
        userName = request.POST.get('name')
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
            messages.success(request,"Sent Successfully")
            return render(request, 'courses/contactFormPage.html', {
                'student':student,
                "message": "Sent Successfully"
            })

        except:
            messages.warning(request,"An Error Occured ")
            return render(request, 'courses/contactFormPage.html', {
                'student':student,
                "message": "An Error Occured ... Try Again Later"
            })


    return render(request,'courses/contactFormPage.html',{
        'student':student,
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
