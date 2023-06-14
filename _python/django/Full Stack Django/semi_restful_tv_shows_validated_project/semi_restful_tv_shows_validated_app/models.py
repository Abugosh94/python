from django.db import models
from datetime import datetime

class MovieManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        all_movies = Movie.objects.all()
        for movie in all_movies:
            if postData['title'].upper() == movie.title.upper():
                errors['duplicate'] = "A show with the same title already exists"
        if len(postData['title']) < 2:
            errors['title'] = "Show title should  be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should  be at least 3 characters"
        if len(postData['desc']) < 10 and len(postData['desc'])!= 0:
            errors['desc'] = "Description should  be at least 10 characters or empty"
        if datetime.strptime(postData['release_date'], "%Y-%m-%d") > datetime.now():
            errors['release_date'] = "Release date should be a past date"
        return errors

class Movie(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="null")
    network = models.CharField(max_length=255)
    release_date = models.DateField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MovieManager()
