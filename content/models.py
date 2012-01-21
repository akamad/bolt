from django.db import models
from django.contrib.auth.models import  User
# Create your models here.


class Tag(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    datetime = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        self.name
    
class UserTag(models.Model):
    user = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)
    def __unicode_(self):
        self.user + self.tag