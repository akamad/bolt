from django.db import models

# Create your models here.
class fb_profile(models.Model):
    uid = models.CharField(max_length=120)
    name = models.Charfield(max_length=100)
    first_name = models.Charfield(max_length=100)
    