from pyexpat import model
from django.contrib import admin
from .models import  Level, Message, Subject

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display= ['sender','email','subject','deliverdTime','isSeen']
    list_display_links= ['sender','email','subject']
    search_fields=['sender']
    list_filter = ['isSeen','deliverdTime']

class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display= ['id','title','creationTime','active']
    list_display_links= ['id','title']
    search_fields=['id','title']
    list_filter = ['creationTime','active']

admin.site.register(Subject,SubjectAdmin)
admin.site.register(Level)
admin.site.register(Message,MessageAdmin)



admin.site.site_header='Header Name'
admin.site.site_title='Site Name'