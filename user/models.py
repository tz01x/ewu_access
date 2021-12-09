from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile' ,on_delete=models.CASCADE)
    university_id=models.CharField(max_length=13)
    