

from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from pages.models import Level
from datetime import datetime
# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self,email,first_name,last_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_admin(email,first_name,last_name,password,**other_fields)


    def create_admin(self,email,first_name,last_name,password,**other_fields):
        if not email:
            raise ValueError(_('You must provide an email address.'))

        email = self.normalize_email(email)
        admin = Admin(email=email,username=first_name+" "+last_name,first_name=first_name,last_name=last_name,**other_fields)
        admin.set_password(password)
        admin.set_visible_password(password)
        admin.save()
        return admin

    def create_student(self,mail,first_name,last_name,password,phone,parent_phone,gender,levelObject,address,school_name):
        if not mail:
            raise ValueError(_('You must provide an email address.'))

        email = self.normalize_email(mail)
        student = Student(
                username=first_name+" "+last_name,
                last_name=last_name,
                first_name=first_name,
                email=email,
                phone= phone,
                gender=gender,
                parentPhone=parent_phone,
                level=levelObject,
                address=address,
                schoolname=school_name
            )

        student.set_password(password)
        student.save()

        return student


GENDER=[
    ('male','MALE'),
    ('female','FEMALE'),
]


#AbstractUser._meta.get_field('email')._unique = True

class User(AbstractBaseUser,PermissionsMixin):
    
    username = models.CharField(max_length=200,error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',verbose_name="Full Name")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(_('Email Address'), unique=True)
    password = models.CharField(max_length=100)
    raw_password = models.CharField(max_length=100)
    phone = models.CharField(max_length=11,unique=True)
    gender = models.CharField(max_length=10,choices=GENDER)
    is_staff = models.BooleanField(default=False,help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    is_active = models.BooleanField(default=True,help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    date_joined = models.DateTimeField(default=timezone.now,verbose_name='Date joined')
   
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    class Meta:
        verbose_name = 'All Users'
        #plural_name = 'All Users'
        ordering=['id']

    objects = CustomAccountManager()

    def set_first_name(self,first_name):
        self.first_name = first_name

    def set_last_name(self,last_name):
        self.last_name = last_name

    def set_username(self,username):
        self.username = username

    def set_gender(self,gender):
        self.gender = gender

    def set_email(self,email):
        self.email = email

    def set_visible_password(self,password):
        self.raw_password = password

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return f"{self.username} "



class Admin(User):
    
    class Meta:
        verbose_name = 'Admin'

    def __str__(self):
        return f"{self.username} "


class Student(User):
    
    
    #code = models.CharField(max_length=5)
    level = models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Education level')
    parentPhone =models.CharField(max_length=14,verbose_name="Parent's Phone")
    schoolname = models.CharField(max_length=100,verbose_name='School Name')
    address = models.TextField(max_length=500,blank=True,null =True)
    #is_verified = models.BooleanField(default=False , verbose_name="Email Verified")
    
    class Meta:
        verbose_name = 'Student'

    def set_Educational_Level(self,level):
        self.level = level

    def set_Phone(self,phone):
        self.phone = phone

    def set_Parent_Phone(self,parentPhone):
        self.parentPhone = parentPhone

    def set_School_Name(self,schoolname):
        self.schoolname = schoolname
    
    def set_Address(self,address):
        self.address = address

    def __str__(self):
        return f"{self.username} "


LOGIN_METHODS = [
    ('email','By Email'),
    ('code','By Code'),
]
class Login(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User')
    level = models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Education level')
    email = models.EmailField(max_length=50)
    loginMethod = models.CharField(max_length=10,choices=LOGIN_METHODS)
    loginTime = models.DateTimeField(default=datetime.now,verbose_name='Login Time')

    class Meta:
        ordering =['id']
        unique_together=(("user","email","loginTime"),)

    def set_login_method(self,method):
        self.loginMethod = method

    def  __str__(self):
        return f"User : {self.user} , Email : {self.email}"
