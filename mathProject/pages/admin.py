from pyexpat import model
from django.contrib import admin
from .models import  Level, Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display= ['sender','email','subject','deliverdTime','isSeen']
    list_display_links= ['sender','email','subject']
    search_fields=['sender']
    list_filter = ['isSeen','deliverdTime']


admin.site.register(Level)
admin.site.register(Message,MessageAdmin)



admin.site.site_header='Header Name'
admin.site.site_title='Site Name'