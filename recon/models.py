from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Suser(AbstractUser):
    username = models.CharField('用户名',max_length=64,unique=True)

    def __str__(self):
        return self.username


class Surl(models.Model):
    pass
