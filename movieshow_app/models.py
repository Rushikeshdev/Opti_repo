from distutils.command.upload import upload
from typing_extensions import runtime
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255,blank=False,null=False)
    poster = models.ImageField(upload_to='media/')
    genre = models.CharField(max_length=255,blank=False,null=False)
    rating = models.FloatField()
    release_year = models.IntegerField()
    metacrictic_rating = models.FloatField()
    runtime_movie = models.IntegerField()

    def __str__(self):
        return f"Moives {self.title}"

