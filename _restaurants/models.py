from django.db import models
from django.shortcuts import reverse


class Cuisine(models.Model):
    title = models.CharField(max_length=100, default='default')
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cuisine', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Cuisine'
        verbose_name_plural = 'Cuisines'


class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default=None)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True, blank=True, related_name='restaurants')
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100)
    website = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('restaurant_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
