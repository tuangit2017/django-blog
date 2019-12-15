from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True,default= 'users/default.jpg', null=True,)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
