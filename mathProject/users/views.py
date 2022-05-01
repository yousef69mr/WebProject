
from django.http import  JsonResponse
from .models import User
# Create your views here.

def getUsers(request):
    users = User.objects.all()
    return JsonResponse({
        "students":list(users.values())
    })