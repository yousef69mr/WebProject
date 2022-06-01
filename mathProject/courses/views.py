
from datetime import date
import os

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .validators import get_valid_image_extensions
from users.models import Login, Student,User,Admin
from users.views import getDataOfGender
from .models import File, Lecture,RegisteredLecture,Rating
from pages.models import Message,Level, Subject

from operator import attrgetter
from itertools import chain

# Create your views here.

def getFiles(request):
    files = File.objects.all()
    return JsonResponse({
        "files":list(files.values())
    })


    
def getNumberOfStudentsSignedToSubject(subjects):
    
    arrayOfData = []
    for i in range(len(subjects)):
        regesteredlectures = RegisteredLecture.objects.all().filter(lecture__branch = subjects[i])

        arrayOfData.append(regesteredlectures.count())

    #print(arrayOfData)

    return arrayOfData

def getNumberOfFilesSignedToSubject(subjects):

    arrayOfData = []
    for i in range(len(subjects)):
        files = File.objects.all().filter(branch = subjects[i])

        arrayOfData.append(files.count())

    #print(arrayOfData)

    return arrayOfData

def sumOfList(List):
    sum=0
    for i in range(len(List)):
        sum+=int(List[i])

    return sum

def calculateAverageRatings():

    rates = Rating.objects.all().values_list('score',flat=True)
    print(rates)
    #print(list(rates))
    sum =sumOfList(list(rates))
    numOfRates = rates.count()
    result = sum/numOfRates

    return result
    

def getRating():
    #print("rates")
    rates =Rating.objects.all()
    one = rates.filter(score=1).count()
    two = rates.filter(score=2).count()
    three = rates.filter(score=3).count()
    four = rates.filter(score=4).count()
    five = rates.filter(score=5).count()
    result = [five,four,three,two,one]
    #print(result)
    return result

def calculateSumOfList(List):
    sum =0

    for i in range(len(List)):
        sum+=List[i]

    return sum
    
    

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
        
    
    try:
        
        user = get_object_or_404(Student,id=request.user.id)
        print(user)
    except:
        user = get_object_or_404(Admin,id=request.user.id)
        print(user)

    registered = RegisteredLecture.objects.filter(user=user)
    lectures = registered.values_list('lecture',flat=True)
    #print(registered)
    #print(lectures)
    files = File.objects.all()
    
    if user.is_superuser :
        return render(request,'courses/lectures.html',{
        'student':user,
        'lectures':Lecture.objects.all(),
        'registeredLectures': lectures,
        'files':files,

        })

    if hasattr(user,'level'):

        return render(request,'courses/lectures.html',{
            'student':user,
            'lectures':Lecture.objects.filter(gradeLevel=user.level),
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
    
    if student.is_superuser:
        
        levels = Level.objects.all()
        
        genderData = getDataOfGender(request)
        averageRatings = calculateAverageRatings()
        subjects = Subject.objects.all()
        #print(subjects)
        subjectList = list(subjects.values_list('title',flat=True))
        #print(subjectList)
        numberOfStudentsSignedToSubject = getNumberOfStudentsSignedToSubject(subjects)
        numberOfFilesSignedToSubject = getNumberOfFilesSignedToSubject(subjects)
        today =  date.today()
        #print(d.day)
        admins = Admin.objects.all()
        students = Student.objects.all()
        lectures = Lecture.objects.all()
        numberOfStudents = students.count()
        numberOfLectures = lectures.count()
        numberOfFiles = File.objects.all().count()
        dailyLogins = Login.objects.filter(loginTime__day = today.day).count()

        listOfRatings = getRating()

        #print(dailyLogins)
        mostActiveLectures = sorted(lectures,
        key=attrgetter('signed'))
        
        return render(request,'courses/dashboard.html',{
            'levels':levels,
            'student':student,
            'students':students.reverse(),
            'lectures': lectures.reverse(),
            'numberOfSubjects':subjects.count(),
            'averageRatings':averageRatings,
            'numberOfStudents':numberOfStudents,
            'numberOfAdmins':admins.count(),
            'numberOfLectures':numberOfLectures,
            'numberOfFiles':numberOfFiles,
            'dailyLogins':dailyLogins,
            'star_1':listOfRatings[4],
            'star_2':listOfRatings[3],
            'star_3':listOfRatings[2],
            'star_4':listOfRatings[1],
            'star_5':listOfRatings[0],
            'totalRatings':calculateSumOfList(listOfRatings),
            'rankedData':reversed(mostActiveLectures),
            'chart_1':genderData,
            'subjects':subjectList,
            'chart_2':numberOfStudentsSignedToSubject,
            'chart_3':numberOfFilesSignedToSubject,
            'chart_5':listOfRatings,
            


        })

    else:
        student = get_object_or_404(Student,id=request.user.id)
        lectures = Lecture.objects.filter(gradeLevel=student.level)
        #files = File.objects.filter(level=student.level)
        
        return render(request,'courses/dashboard.html',{
        'student':student,
        'lectures':reversed(lectures),
    })

    




def editProfilePage(request):

    levels=Level.objects.all()

    if not request.user.is_authenticated:

        return redirect(reverse("login"))
    
   
    try:
        
        user = get_object_or_404(Student,id=request.user.id)
        print(user)
    except:
        user = get_object_or_404(Admin,id=request.user.id)
        print(user)

    print(user.username)
    
    if request.method == "POST":

        profileImage = request.FILES.get('profile_image')
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
        print(profileImage)

        

        print(profileImage)
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

        if Pass != Pass2 :
            return render(request, 'courses/editProfile.html', {
                "levels":levels,
                "message":"Two Passwords don't match",
                "alertType":"alert-danger",
                'student':user,

            })

        extenstion = os.path.splitext(profileImage.name)[1]
        print(extenstion)

        validate_extension = get_valid_image_extensions()

        if not extenstion.lower() in  validate_extension:

            print("Invalid Extension")
            return render(request, 'courses/editProfile.html', {
                "levels":levels,
                "message":"Picture Extension is Invalid",
                "alertType":"alert-danger",
                'student':user,

            })
       

        try:
      
            #print("here")
            if hasattr(user,'level'):
  
                levelObject = Level.objects.get(levelCode=level)

                Student.objects.filter(id=request.user.id).update(
                    username = username,
                    full_name=fname+" "+lname,
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

            else:
                
                Admin.objects.filter(id=request.user.id).update(
                    username = username,
                    full_name=fname+" "+lname,
                    last_name=lname,
                    first_name=fname,
                    email=mail.lower(),
                    #raw_password=Pass,
                    phone=phone,
                    gender=gender,
                )

                
            user.set_visible_password(Pass)
            user.set_password(Pass)
            if profileImage:
                user.set_profile_image(profileImage)

            
            
            user.save()
            print(user.email)
            updatedUser = authenticate(request,username=user.email,password=Pass)
            login(request,updatedUser)
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
            'student':updatedUser,
        })

        except:

            return render(request, 'courses/editProfile.html', {
                "levels":levels,
                "message":"An Error Occured during Registeration",
                "alertType":"alert-danger",
                'student':user,

            })
        

    return render(request,'courses/editProfile.html',{
        "levels":levels,
        "message":"",
        "alertType":"",
        'student':user,
    })



def contactUsPage(request):
     
    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
        
    user = get_object_or_404(User,id=request.user.id)

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
                'student':user,
                "message": "Sent Successfully"
            })

        except:
            messages.warning(request,"An Error Occured ")
            return render(request, 'courses/contactFormPage.html', {
                'student':user,
                "message": "An Error Occured ... Try Again Later"
            })


    return render(request,'courses/contactFormPage.html',{
        'student':user,
    })


def lecturesTable(request):

    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
    user = get_object_or_404(User,id=request.user.id)

    if user.is_superuser:
    
        lectures = Lecture.objects.all()
        levels = Level.objects.all()
        subjects = Subject.objects.all()

        return render(request,'courses/lecturesTable.html',{
            'lectures':lectures.reverse(),
            'student':user,
            'levels':levels,
            'subjects':subjects,
        })



def profileCards(request):

    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
    user = get_object_or_404(User,id=request.user.id)

    if user.is_superuser:
    
        
        admins = Admin.objects.all()
        students = Student.objects.all()
        
        users = sorted(
        chain(admins, students),
        key=attrgetter('id'))
        
        print(users)

        return render(request,'courses/profileCards.html',{
            'users':users,
            'student':user,
        })

    else:
        return render(request,'courses/error.html',{
            'student':user,
        })


def rateSystem(request):
     
    if not request.user.is_authenticated:

        return redirect(reverse("login"))
        
        
    user = get_object_or_404(User,id=request.user.id)
    #print(user)

    if request.method == "POST":
        

        value = request.POST.get('rate')
        #print(value)

        id = request.POST.get('id')
        username = request.POST.get('username')
        description = request.POST.get('description')
        

        print(id)
        print(username)
        print(description)


        try:
            rate = get_object_or_404(Rating,user__id=user.id)
            #print(rate)
        except:
            rate = None


        if rate == None:

   
            try:
                rate = Rating(user=user,score=value,description=description)
                
                #print(rate)
                rate.save()
                
                return render(request, 'courses/rateSystem.html', {
                    'student':user,
                    'clicked':True,
                    "message": "Thanks for rating us!"
                })

            except:
                
                return render(request, 'courses/rateSystem.html', {
                    'student':user,
                    'clicked':True,
                    "message": "An Error Occured ... Try Again Later"
                })

        else:
            
            try:
                rate.set_score(value)
                rate.set_description(description)
                #print(rate)
                rate.save()
                
                return render(request, 'courses/rateSystem.html', {
                    'student':user,
                    'clicked':True,
                    "message": "Thanks for rating us!"
                })

            except:
                
                return render(request, 'courses/rateSystem.html', {
                    'student':user,
                    'clicked':True,
                    "message": "An Error Occured ... Try Again Later"
                })




    return render(request,'courses/rateSystem.html',{
        'student':user,
        "alertType":"",
        'clicked':False,

    })
