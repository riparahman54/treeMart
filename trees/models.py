from django.db import models

# Create your models here.
class Tree(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='tree_images/', null = True, blank=True)

    def __str__(self):
        return self.name
