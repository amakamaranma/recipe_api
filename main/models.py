from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    ingredient = models.CharField(max_length=200)
    tags = models.CharField(max_length=60)


    def __str__(self):
        return self.name
