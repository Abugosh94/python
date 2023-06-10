from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, default="Old dojo")

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
