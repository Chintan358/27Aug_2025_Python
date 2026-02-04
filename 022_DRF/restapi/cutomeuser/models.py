from django.db import models
from django.contrib.auth.models import AbstractUser
from cutomeuser.manage import CustomUserManager


class RoleManager(models.Model):
    name = models.CharField(max_length=20)

class CustomeUser(AbstractUser):
    Username = None
    phone = models.CharField(max_length=15,unique=True)
    bio = models.TextField(null=True)
    role = models.ForeignKey(RoleManager,on_delete=models.CASCADE,null=True)

    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()
