
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponseRedirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth import logout

from users.models import Student
from .models import File, Lecture,RegisteredLecture
from pages.models import Message
# Create your views here.

def getFiles(request):
    files = File.objects.all()
    return JsonResponse({
        "files":list(files.values())
    })

def lecture(request,lecture_id):
    
    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        

    student = get_object_or_404(Student,id=request.user.id)
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
        

    student = get_object_or_404(Student,id=request.user.id)
    registered = RegisteredLecture.objects.filter(user=student)
    lectures = registered.values_list('lecture',flat=True)
    #print(registered)
    #print(lectures)
    files = File.objects.all()
    
    return render(request,'courses/lectures.html',{
        'student':student,
        'lectures':Lecture.objects.filter(gradeLevel=student.level),
        'registeredLectures': lectures,
        'files':files,

    })

def regesteredlectures(request):

    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
    student = get_object_or_404(Student,id=request.user.id)
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
        
    student = get_object_or_404(Student,id=request.user.id)
    
    return render(request,'courses/dashboard.html',{
        'student':student,
    })



def contactUsPage(request):
     
    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
        
    student = get_object_or_404(Student,id=request.user.id)

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