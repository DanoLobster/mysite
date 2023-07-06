from django.db import models
from django.contrib.auth.models import User
from django import forms

CATEGORY_CHOICES = [
    ('headwear', 'Headwear'),
    ('neckwear', 'Neckwear'),
    ('top', 'Top'),
    ('bottom', 'Bottom'),
    ('legwear', 'Legwear'),
    ('feetwear', 'Feetwear'),
    ('underwear', 'Underwear'),
    ('accessory', 'Accessory'),
    ('other', 'Other'),
]

class Clothing(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    image = models.ImageField(upload_to='clothing_images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Outfit(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='clothing_images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name