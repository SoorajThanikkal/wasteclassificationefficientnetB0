from django.db import models

# Create your models here.
class User(models.Model):
    profile_picture = models.ImageField(upload_to='profile_picture/',null=True, blank=True)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phonenumber = models.IntegerField()
    place = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Waste(models.Model):
    waste_image = models.ImageField(upload_to='waste/')
    
