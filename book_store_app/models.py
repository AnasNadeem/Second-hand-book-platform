from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100)

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=250)
    cash_price = models.IntegerField()
    coin_price = models.IntegerField(blank=True)
    # image = models.ImageField()

class BookDescription(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # more_image = 
    # video_or_gif = 
    publisher = models.CharField(max_length=250, blank=True)
    published_date = models.DateField(blank=True)
    mass = models.IntegerField(blank=True)
    author_name = models.CharField(max_length=200, blank=True)

    