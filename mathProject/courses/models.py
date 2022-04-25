from asyncio.windows_events import NULL
import os
from django.db import connection
from django.shortcuts import redirect
from datetime import datetime
from django.db import models
from django.urls import reverse
from .validators import validate_file_extension,validate_image_file_extension
from pages.models import Level
from users.models import Student

# Create your models here.

MATH_BRANCHES=(
    ('algebra','ALGEBRA'),
    ('trignometry','TRIGNOMETRY'),
    ('geometry','GEOMETRY'),
)

class Lecture(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(default="media/defaults/photo-1429043794791-eb8f26f44081.jpeg",upload_to='media/photos/%y/%m/%d', validators=[validate_image_file_extension],verbose_name="Thumbnail",null=True)
    branch=models.CharField(max_length=25,choices=MATH_BRANCHES,verbose_name='category')
    sourceLink=models.CharField(max_length=400)
    gradeLevel=models.ForeignKey(Level,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    creationTime =models.DateTimeField(default=datetime.now)

    def  __str__(self):
        return f" {self.title} ({self.branch})"
        
    class Meta:
        ordering=['id']



class RegisteredLecture(models.Model):

    user=models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name='Student')
    lecture =models.ForeignKey(Lecture,on_delete=models.CASCADE,default=NULL)
    regesterTime =models.DateTimeField(default=datetime.now)

    class Meta:
        ordering=['id']
        unique_together = (("user", "lecture"),)

    def get_absolute_url(self):
        return reverse("lecture", kwargs={'lecture_id':self.id})

    def  __str__(self):
        return f"({self.user.id}) , ({self.lecture.id})"


class File(models.Model):
    lecture=models.ForeignKey(Lecture,on_delete=models.CASCADE,default=NULL)
    file =models.FileField(default=NULL,upload_to='media/files/%Y/%m/%d/', validators=[validate_file_extension])
    level = models.ForeignKey(Level,on_delete=models.CASCADE,default=NULL)
    branch=models.CharField(max_length=25,choices=MATH_BRANCHES,verbose_name='category')
    uploadTime =models.DateTimeField(default=datetime.now)
    isActive=models.BooleanField(default=True)

    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {File} CASCADE'.format(cls._meta.db_table))

    class Meta:
        ordering=['id']
        unique_together = (("file", "lecture"),)

    def filename(self):
        return os.path.basename(self.file.name)

    def get_absolute_path(self):
        return redirect(self.file)

    def  __str__(self):
        return f"{self.lecture.id}) , ({self.file})"