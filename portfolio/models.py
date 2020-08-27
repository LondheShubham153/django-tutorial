from django.db import models

# Create your models here.

class Job(models.Model):
    company = models.CharField(max_length=250,blank=True,null=True)
    description = models.CharField(max_length=250,blank=True,null=True)
    image = models.ImageField(upload_to='images/')
    