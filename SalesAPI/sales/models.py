from django.db import models
from product.models import Product
# Create your models here.

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)  # e.g., Pack, Carton
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.quantity_sold} {self.product.product_name} at {self.selling_price} each"
