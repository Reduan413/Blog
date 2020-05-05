from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField()
    body = models.TextField()