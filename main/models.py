import uuid
from django.db import models

class Shop(models.Model):
    CATEGORY_CHOICES = [
        ('New Item', 'New Item'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()