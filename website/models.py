from django.db import models

# Create your models here.
class About(models.Model): 
    title = models.CharField(max_length=127)
    sub_title_1 = models.CharField(max_length=127)
    content_1 = models.TextField()
    sub_title_2 = models.CharField(max_length=127)
    content_2 = models.TextField()

class Project(models.Model): 
    title = models.CharField(max_length=127)
    sub_title = models.CharField(max_length=127)
    link = models.CharField(max_length=127)
    image = models.ImageField(upload_to='website/static/images/')