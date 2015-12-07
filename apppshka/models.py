#-*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class App_new(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.TextField()
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.field1

class Comments(models.Model):
    comment_content = models.TextField()
    comment_author = models.CharField(max_length=35)
    page = models.ForeignKey(App_new, blank=True, null=True)

    def __str__(self):
        return (self.comment_content).encode('utf-8', errors='replace')


