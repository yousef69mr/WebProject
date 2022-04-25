from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.sideBar,name="sideBar"),
    path('navbar',views.navBar,name="navBar"),
    path('levelCards',views.levelCard,name="levelCard"),
    path('footer',views.footer,name="footer"),
    #path('contactUs',views.contactUs,name="contactUs"),
    
]
