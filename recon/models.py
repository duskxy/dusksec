from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Suser(AbstractUser):
    username = models.CharField('用户名',max_length=64,unique=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'suser'

class Surl(models.Model):
    url = models.URLField('查询域名',max_length=200)
    def __str__(self):
        return self.url
    class Meta:
        db_table = 'surl'

class Sudata(models.Model):
    uid = models.ForeignKey(Surl,verbose_name='域名',blank=True,null=True,on_delete=models.CASCADE)
    uda = models.URLField('子域名','url')
    def __str__(self):
        return self.uda
    class Meta:
        db_table = 'sudata'
