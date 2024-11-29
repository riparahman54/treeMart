# models.py
from django.db import models
from django.contrib.auth.models import User

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
    description = models.TextField(blank=True, null=True)
    care_tips = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='tree_images/', null=True, blank=True)
    total_rating = models.IntegerField(default=0)
    num_ratings = models.IntegerField(default=0)

    @property
    def average_rating(self):
        """Calculate the average rating."""
        if self.num_ratings == 0:
            return 0
        return round(self.total_rating / self.num_ratings, 1)

    def __str__(self):
        return self.name


class Rating(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.tree.name}: {self.rating}'
