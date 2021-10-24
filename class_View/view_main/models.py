from django.db import models
from django.db.models.base import Model
from django.db.models.fields import related
from django.urls import reverse


class musician(models.Model):
    FirstName= models.CharField(max_length=20)
    LastName= models.CharField(max_length=30)
    instument=models.CharField(max_length=20)


    def __str__(self):
        return self.FirstName

    def get_absolute_url(self):
        return reverse("index")
        
    
class Album(models.Model):
    arist=models.ForeignKey(musician,on_delete=models.CASCADE,related_name='album_list')
    name=models.CharField(max_length=30)
    release_date=models.DateField()


    def __str__(self):
        return self.name
