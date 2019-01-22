from django.db import models
from django.contrib.postgres.fields import ArrayField


class Partner(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    cats = ArrayField(models.CharField(max_length=100))
    about = models.TextField(blank=True)
    rating = models.IntegerField(default=3)
    main_photo = models.ImageField(
        upload_to='partners_profile', default='default.svg')
    # list of images
    list_images = ArrayField(
        models.CharField(max_length=300, blank=True), blank=True, null=True)

    def __str__(self):
        return self.name
