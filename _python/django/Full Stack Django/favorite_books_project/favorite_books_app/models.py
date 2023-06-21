from django.db import models
from login_and_regestration_app.models import *

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="Null")
    uploaded_by = models.ForeignKey(User,related_name="uploaded_by", on_delete = models.CASCADE)
    favorites = models.ManyToManyField(User,related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
