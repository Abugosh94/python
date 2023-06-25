from django.db import models
from login_and_regestration_app.models import * 

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    description = models.TextField(default="null")
    rating = models.IntegerField(default=1)
    user = models.ForeignKey(User, related_name="reviews", on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name="reviews", on_delete = models.CASCADE, default = 1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)