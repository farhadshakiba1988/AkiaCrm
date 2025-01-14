from django.db import models

from web.models import Sale


class SaleItem(models.Model):
    """Model for individual items in a sale"""
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def calculate_total(self):
        """Calculate total for this item including discount"""
        subtotal = self.quantity * self.unit_price
        discount = subtotal * (self.discount_percentage / 100)
        return subtotal - discount
