from django.urls import path
from .import views

urlpatterns = [
    path('getUsers',views.getUsers,name="getUsers"),
    path('password/',views.getUsers),
]
