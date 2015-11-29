from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class App_new (models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.field1