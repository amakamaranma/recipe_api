from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    ingredients = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.name
