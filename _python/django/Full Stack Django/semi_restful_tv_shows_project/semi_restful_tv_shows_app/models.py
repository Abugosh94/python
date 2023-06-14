from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="null")
    network = models.CharField(max_length=255)
    release_date = models.DateField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
