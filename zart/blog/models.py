from django.db import models
from datetime import date
# Create your models here.
class post(models.Model):
    id = models.AutoField
    post_title = models.CharField(max_length=500)
    desc = models.CharField(max_length=5000, default="")
    shortdesc = models.CharField(max_length=500, default="")
    link = models.CharField(max_length=100, default="")
    thumbnail = models.ImageField(upload_to='static/blog/images', default="")



