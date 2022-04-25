from pyexpat import model
from django.contrib import admin
from .models import Lecture , RegisteredLecture,File
# Register your models here.

class LectureAdmin(admin.ModelAdmin):
    model = Lecture
    list_display= ['title','gradeLevel','branch','active']
    list_display_links= ['title','gradeLevel']
    list_editable =['branch']
    search_fields=['title']
    list_filter = ['gradeLevel','branch','active']


class FileAdmin(admin.ModelAdmin):
    model = File
    list_display= ['lecture','file','uploadTime','isActive']
    list_display_links= ['lecture','uploadTime']
    search_fields=['file']
    list_filter = ['level','branch','uploadTime','isActive']
    actions = ['truncate']

    def truncate(self,request):
        File.truncate(self)
 

class RegisteredLectureAdmin(admin.ModelAdmin):
    model = RegisteredLecture
    list_display= ['user','lecture','regesterTime']
    list_display_links= ['user','lecture']
    #list_editable =['file']
    search_fields=['user']
    


admin.site.register(Lecture,LectureAdmin)
admin.site.register(RegisteredLecture,RegisteredLectureAdmin)
admin.site.register(File,FileAdmin)
