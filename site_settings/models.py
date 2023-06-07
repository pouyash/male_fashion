from django.db import models

# Create your models here.
from product.models import Product


class Slider(models.Model):
    product = models.OneToOneField(Product, related_name='slider', on_delete=models.CASCADE)
    header = models.CharField(max_length=300)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.header} + {str(self.product)}'