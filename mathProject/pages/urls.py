from django.urls import path
from .import views

from django.views.generic.base import TemplateView #import TemplateView

urlpatterns = [
   
    path('',views.index,name="index"),
    path('about',views.aboutPage,name="about"),
    path('login',views.loginPage,name="login"),
    path('signup',views.signupPage,name="signup"),
    path('contactUs',views.contactUsPage,name="contactUs"),
    path('error',views.errorPage,name="error"),
    path('redirect',views.redirect_view),
    
    path("robots.txt",TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain")),  #add the robots.txt file
]
