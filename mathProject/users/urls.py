from django.urls import path
from .import views

urlpatterns = [
    path('getStudents',views.getStudents,name="getStudents"),
    path('password/',views.getStudents),
]
