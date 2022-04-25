from django.shortcuts import render
from pages.models import Level,Message
# Create your views here.

def sideBar(request):
    return render(request,'parts/sideBar.html',{
        'name' :'ahmed mohamed'
    })

def navBar(request):
    return render(request,'parts/navBar.html')

def levelCard(request):
    levels=Level.objects.all()
    return render(request,'parts/levelsCards.html',{
        'levels' :levels
    })

def footer(request):
    
    return render(request,'parts/footer.html')

def contactUs(request):
    
    if request.method == "POST":
        userName = request.POST['name']
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('message')

        #print(userName)
        #print(phone)
        #print(email)
        #print(subject)
        #print(content)

        try:
            message = Message(sender=userName,email=email,phone=phone,message=content,subject=subject)
            message.save()

        except:
            return render(request, 'pages/index.html', {
                "message": "Username already taken."
            })


    return render(request,'pages/index.html')
