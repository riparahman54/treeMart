from django.db import models

# Create your models here.
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
    image = models.ImageField(upload_to='tree_images/', null = True, blank=True)

    def __str__(self):
        return self.name
