from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    categories = models.ManyToManyField(Category)
    created_date = models.DateField()
    age_limit = models.PositiveIntegerField()