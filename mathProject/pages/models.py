from asyncio.windows_events import NULL
from django.db import models
from datetime import datetime


# Create your models here.
GRADE_LEVEL_FULL_NAME =(
    ('1st preparatory','1ST PREPARATORY'),
    ('2nd preparatory','2ND PREPARATORY'),
    ('3rd preparatory','3RD PREPARATORY'),
    ('1st secondary','1ST SECONDARY'),
    ('2nd secondary','2ND SECONDARY'),
    ('3rd secondary','3RD SECONDARY'),
)

GRADE_LEVEL =(
    ('1P','1ST_PREP'),
    ('2P','2ND_PREP'),
    ('3P','3RD_PREP'),
    ('1S','1ST_SEC'),
    ('2S','2ND_SEC'),
    ('3S','3RD_SEC'),
)
NUMBERS_IN_LETTERS=(
    ('one','ONE'),
    ('two','TWO'),
    ('three','THREE'),
)

LEVELS_IN_LETTERS=(
    ('primary','PRIMARY'),
    ('preparatory','PREPARATORY'),
    ('secondary','SECONDARY'),
)

class Level(models.Model):

    levelCode=models.CharField(max_length=10,choices=GRADE_LEVEL)
    levelFullName=models.CharField(max_length=25,choices=GRADE_LEVEL_FULL_NAME)
    numberOfLevelInLetters=models.CharField(max_length=10,choices=NUMBERS_IN_LETTERS,default=NULL)
    levelNameInLetters=models.CharField(max_length=15,choices=LEVELS_IN_LETTERS,default=NULL)
    color=models.CharField(max_length=15,default='#64bcf4',verbose_name='Card Color')
    isActive=models.BooleanField(default=True,verbose_name='Active')

    class Meta:
        verbose_name = 'Education level'
        ordering=['id']
        unique_together = (("levelCode", "levelFullName"),("levelNameInLetters","numberOfLevelInLetters"),)

    def  __str__(self):
        return f" {self.levelFullName}"

class Message(models.Model):

    sender = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=11,default=NULL)
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=500)
    respond = models.TextField(null=True,blank=True,verbose_name='Reply')
    isSeen = models.BooleanField(default=False,verbose_name='Seen')
    deliverdTime = models.DateTimeField(default=datetime.now,verbose_name='Delivered Time')

    class Meta:
        ordering=['id']
        unique_together=(("sender","email","phone","subject","message"),)

    def  __str__(self):
        return f"Message Code : {self.id} , Sender Name : {self.sender}"

