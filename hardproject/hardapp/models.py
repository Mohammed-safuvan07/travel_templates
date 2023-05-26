from django.db import models

# Create your models here.
class table(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to="pics")
    desc = models.TextField()

class table2(models.Model):
    name1 = models.CharField(max_length=200)
    img1 = models.ImageField(upload_to="pics")
    desc1 = models.TextField()