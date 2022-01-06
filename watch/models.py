from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.db.models import Q

# Create your models here.

# NeighbourHood Model
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
    
    def create_neighborhood(self):
        """
        A method that creates a neighbourhood
        """
        self.save()
        
    def delete_neighborhood(self):
        """
        A method that deletes a neighbourhood
        """
        self.delete()    
        
    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        """
        A method that finds a neighbourhood using its id
        """
        return cls.objects.filter(id=neighborhood_id) 
    
    @classmethod
    def update_neighbourhood(cls, id):
        """
        A method that updates a neighbourhood
        """
        neighbourhood = cls.objects.filter(id=id).update(id=id)
        return neighbourhood       

# Profile Model
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=250)
    email =  models.CharField(max_length=60)
    phone_number = models.IntegerField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='neighbour', blank=True)
    posted_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.user    