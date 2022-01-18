
from operator import mod
from django.db import models

# Create your models here.
class Comment(models.Model):
    email=models.EmailField()
    content=models.CharField(max_length=50)
    created=models.DateTimeField()


class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=70)

class Event(models.Model):
    description = models.CharField(max_length=50)
    start=models.DateTimeField()
    finish= models.DateTimeField()


class GameRecord(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    score= models.IntegerField()


    