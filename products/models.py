from django.db import models
from django.utils import timezone

# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=256, unique=True)
    category_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to='product_images')
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Продукт: {self.product_name} | Категория: {self.category.category_name}"
