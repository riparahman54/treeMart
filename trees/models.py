# models.py

from django.db import models


class Tree(models.Model):
    SEASON_CHOICES = [
        ('summer', 'Summer'),
        ('winter', 'Winter'),
        ('spring', 'Spring'),
        ('autumn', 'Autumn'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    season = models.CharField(max_length=20, choices=SEASON_CHOICES, default='other')
    description = models.TextField(blank=True, null=True)  # Optional description field
    care_tips = models.TextField(blank=True, null=True)  # Optional care tips field
    image = models.ImageField(upload_to='tree_images/', null=True, blank=True)

    def __str__(self):
        return self.name
