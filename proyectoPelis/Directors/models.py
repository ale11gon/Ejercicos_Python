from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

