from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.

class Profile(AbstractUser):
    
    class Meta:
        verbose_name_plural = 'Profiles'
        verbose_name = 'Profiles'
    
    
