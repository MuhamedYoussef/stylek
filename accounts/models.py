from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=20, default='Select Gender')

    def __str__(self):
        return f'{self.user.username} profile'
