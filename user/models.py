from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    following = models.ManyToManyField("self", symmetrical = False, related_name = 'followers', blank = True)
    bio=models.CharField(max_length=250,blank=True,null=True)
    class Meta:
        db_table = 'User'  
    
    def __str__(self):
        return self.username