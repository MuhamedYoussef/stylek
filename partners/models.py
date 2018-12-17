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
    main_photo = models.ImageField(upload_to='partners_profile', default='default.svg')
    # photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name
