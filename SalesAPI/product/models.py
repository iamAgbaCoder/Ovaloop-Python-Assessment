from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    # Foreign key to a featured product within this category
    item = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True, related_name='product_item')

    def __str__(self):
        # String representation of the Category, used in the admin site
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_measurements = models.JSONField()  # stores as {"Pack": price, "Carton": price}


    def __str__(self):
        # String representation of the Product, used in the admin site
        return self.product_name




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
