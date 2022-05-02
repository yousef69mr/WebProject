from django.urls import path
from .import views

urlpatterns = [
    path('getUsers',views.getUsers,name="getUsers"),
    path("logout", views.logout_view, name="logout"),
    path('activate_user/<uidb64>/<token>',views.activate_user,name='activate'),
]
