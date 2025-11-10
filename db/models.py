import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class Product(models.Model):
    upc = models.CharField(max_length=5, unique=True, help_text="Universal Product Code")
    name = models.CharField(max_length=50, help_text="Product Name")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Product Price")
    
    def __str__(self):
        return f"{self.name} (UPC: {self.upc}) - ${self.price}"
    
    class Meta:
        ordering = ['name']

