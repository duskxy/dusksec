from django.db import models

# Create your models here.

from django.db import models

class Src(models.Model):
    company = models.CharField("src公司",max_length=20,unique=True) 
    url = models.URLField("src网址",max_length=200)

    def __str__(self):
        return self.company
