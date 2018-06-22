from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

Class Suser(AbstractUser):
    username = model.CharField('用户名',max_lenght=64)

    def __str__(self):
        return self.username
