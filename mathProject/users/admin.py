from django.contrib import admin
from .models import Student,Admin,User,Login
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class allUsersAdmin(UserAdmin):
    model = User
    ordering =['id']
    list_display= ['id','username','email','phone','gender','last_login','is_active','is_verified']
    list_display_links= []
    #list_editable =['gender']
    search_fields=['phone','username','email']
    list_filter = ['gender','last_login','is_active','is_verified']

    fieldsets = [

        ('Authentication Info',{
            'classes':('wide',),
            'fields':('username','email','password','raw_password')
        }),
        ('Personal info',{
            'classes':('wide',),
            'fields':('profile_image','full_name','first_name','last_name','gender')
        }),
        ('Contact info',{
            'classes':('wide',),
            'fields':('phone',)
        }),
        ('Permissions',{
            'classes':('wide',),
            'fields':('is_active','is_staff','is_superuser','is_verified')
        }),
        
       
    ]


class StudentAdmin(UserAdmin):
    model = Student
    ordering =['id']
    list_display= ['id','username','email','phone','gender','level','is_active','is_verified']
    list_display_links= ['username','level','email']
    list_editable =['gender']
    search_fields=['phone','username','email']
    list_filter = ['gender','level','is_active','is_verified']

    fieldsets = [
        ('Authentication Info',{
            'fields':('username','email','password','raw_password')
        }),
        ('Personal info',{
            'fields':('profile_image','full_name','first_name','last_name','gender','address')
        }),
        ('Education info',{
            'fields':('level','schoolname')
        }),
        ('Contact info',{
            'fields':('phone','parentPhone')
        }),
        ('Permissions',{
            'fields':('is_active','is_staff','is_superuser','is_verified')
        }),
        ('Important Dates',{
            'fields':('last_login','date_joined')
        }),
    ]


class adminAdmin(UserAdmin):
    
    model = Admin
    ordering =['id']
    list_display= ['id','username','email','phone','gender','is_active','is_verified']
    list_display_links= ['username','email']
    #list_editable =['gender']
    search_fields=['phone','username','email']
    list_filter = ['gender','is_active','is_verified']

    fieldsets = [

        ('Authentication Info',{
            'fields':('username','email','password','raw_password')
        }),
        ('Personal info',{
            'fields':('profile_image','full_name','first_name','last_name','gender')
        }),
        ('Contact info',{
            'fields':('phone',)
        }),
        ('Permissions',{
            'fields':('is_active','is_staff','is_superuser','is_verified')
        }),
        ('Important Dates',{
            'fields':('last_login','date_joined')
        }),
       
    ]

    

class LoginAdmin(admin.ModelAdmin):
    model = Login
    list_display= ['user','email','level','loginMethod','loginTime']
    list_display_links= ['user','email']
    search_fields=['email']
    list_filter = ['level','loginMethod','loginTime']



admin.site.register(Student,StudentAdmin)
admin.site.register(User,allUsersAdmin)
admin.site.register(Admin,adminAdmin)
admin.site.register(Login,LoginAdmin)



