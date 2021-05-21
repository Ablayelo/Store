
from core.settings import TIME_ZONE
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import Settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
# Create your models here.
User = get_user_model()
class Profile(models.Model):
    profile = models.OneToOneField(User,
       verbose_name='Profile', related_name='profile', on_delete=models.SET_NULL,blank=True, null=True)
    image = models.ImageField( verbose_name=_("Photo de profil"),null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Profiles'
        verbose_name = 'Profile'

    def __str__(self):
        return " {0} {1} ".format(self.profile.first_name, self.profile.last_name)
        
def postSaveProfileCreate(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(profile=instance)
    
    
post_save.connect(postSaveProfileCreate, sender=User )
