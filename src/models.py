from django.db import models

# Create your models here.

from django.db import models
status_choices = (
   (1,"正常"),
   (2,"异常")

)



class Src(models.Model):
    company = models.CharField("src公司",max_length=20,unique=True) 
    url = models.URLField("src网址",max_length=200)

    class Meta:
        db_table = "src"
        verbose_name = "src"
        verbose_name_plural = "src"
    def __str__(self):
        return self.company


class asset(models.Model):
    suburl = models.CharField("子域名",max_length=100)
    ip = models.GenericIPAddressField("IP地址")
    url = models.ForeignKey(Src,verbose_name="主域名",on_delete=models.CASCADE)
    status = models.CharField("状态",max_length=10,default=1,choices=status_choices)
    class Meta:
        db_table = "asset"
        verbose_name = "src资产"
        verbose_name_plural = "src资产"

    def __str__(self):
        return self.suburl    
