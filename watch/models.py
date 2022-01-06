from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.db.models import Q

# Create your models here.

class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(User,on_delete = models.CASCADE,related_name='administration',null=True)
    image = CloudinaryField('image')
    description = models.CharField(max_length=250)
    occupants = models.IntegerField(default=0, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 