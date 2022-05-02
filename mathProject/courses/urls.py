from django.urls import path
from .import views

urlpatterns = [
   
    path('lectures/',views.lectures,name="lectures"),
    path('myLectures/',views.regesteredlectures,name="regesteredlectures"),
    path('dashboard/',views.dashboardPage,name="dashboard"),
    path('editProfile/',views.editProfilePage,name="editProfile"),
    path('contactUs/',views.contactUsPage,name="contactus"),
    path('lectures/<int:lecture_id>/',views.lecture,name="lecture"),
    
]
