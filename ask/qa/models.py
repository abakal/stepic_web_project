from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Question(models.Model):
    class Meta:
        db_table='question'
    title=models.CharField(max_length=255)
    text=models.TextField()
    added_at=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(default = 0)
    author=models.ForeignKey(User,related_name='question_athor',blank=True,null=True)
    likes=models.ManyToManyField(User,related_name='question_likes',blank=True)
    def __str__(self):
    	return self.title

class Answer(models.Model):
    class Meta:
        db_table='answer'
    text=models.TextField()
    added_at=models.DateTimeField(auto_now_add=True)
    question=models.ForeignKey(Question)
    author=models.ForeignKey(User)

    
    
    
    
    
    
