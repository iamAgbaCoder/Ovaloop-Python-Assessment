from django.db import models
        
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  

    def __str__(self):
        # String representation of the Product, used in the admin site
        return self.product_name
    

class UnitMeasurement(models.Model):
    product = models.ForeignKey(Product, related_name='unit_measurements', on_delete=models.CASCADE)
    unit_type = models.CharField(max_length=50)  # e.g., "Pack", "Carton"
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)



class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='batches')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation of the Batch, used in the admin site
        return self.product

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'

        ordering = ["-created_at"]
