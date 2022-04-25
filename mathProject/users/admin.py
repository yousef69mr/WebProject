from django.contrib import admin
from .models import Student,Admin,User,Login
from django.contrib.auth.admin import UserAdmin
from .forms import AdminUserChangeForm

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display= ['id','username','email','gender','level']
    list_display_links= ['username','level','email']
    list_editable =['gender']
    search_fields=['phone']
    list_filter = ['gender','level']

    fieldsets = [
        ('Authentication Info',{
            'fields':('email','password')
        }),
        ('Personal info',{
            'fields':('username','first_name','last_name','gender','address')
        }),
        ('Education info',{
            'fields':('level','schoolname')
        }),
        ('Contact info',{
            'fields':('phone','parentPhone')
        }),
        ('Permissions',{
            'fields':('is_active','is_staff','is_superuser')
        }),
        ('Important Dates',{
            'fields':('last_login','date_joined')
        }),
    ]

    form = AdminUserChangeForm
    #add_form = AdminUserCreationForm()



class LoginAdmin(admin.ModelAdmin):
    model = Login
    list_display= ['user','email','level','loginMethod','loginTime']
    list_display_links= ['user','email']
    search_fields=['email']
    list_filter = ['level','loginMethod','loginTime']




admin.site.register(Student,StudentAdmin)
admin.site.register(User)
admin.site.register(Admin,UserAdmin)
admin.site.register(Login,LoginAdmin)


