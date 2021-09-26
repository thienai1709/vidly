from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(modes.Model):
    title = models.CharField(max_length=255)
    released_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(to=Genre, on_delete=models.CASCADE)
