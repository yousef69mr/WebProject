from django.urls import path
from .import views

urlpatterns = [
    path('getDataOfGender',views.getDataOfGender,name="getDataOfGender"),
    path('getUsers',views.getUsers,name="getUsers"),
    path("logout", views.logout_view, name="logout"),
    path('activate_user/<uidb64>/<token>',views.activate_user,name='activate'),
    #path("reset-password", views.reset_password, name="resetPassword"),
    path("request-reset-link", views.RequestPasswordResetEmail.as_view(), name="request-password"),
    path('set_new_password/<uidb64>/<token>',views.set_new_password,name='reset-user-password'),
]
