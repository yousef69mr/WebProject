
from django.http import  JsonResponse
from .models import Student
# Create your views here.

def getStudents(request):
    students = Student.objects.all()
    return JsonResponse({
        "students":list(students.values())
    })