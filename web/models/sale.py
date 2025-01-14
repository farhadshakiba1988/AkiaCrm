from django.db import models
from django.utils import timezone

from web.config.constants import SaleStatus
from web.models import Customer, Employee


class Sale(models.Model):
    """Model for tracking sales"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    invoice_number = models.CharField(max_length=20, unique=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=50)
    currency = models.CharField(max_length=3, default='IRR')
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4, default=1)

    def calculate_total_with_tax_and_discount(self):
        """Calculate final sale amount including tax and discount"""
        subtotal = self.total_amount
        discount = subtotal * (self.discount_percentage / 100)
        after_discount = subtotal - discount
        tax = after_discount * (self.tax_percentage / 100)
        return after_discount + tax + self.shipping_cost

    def get_payment_status(self):
        """Get detailed payment status"""
        if not self.payment_date:
            if timezone.now().date() > self.due_date:
                days_overdue = (timezone.now().date() - self.due_date).days
                return f'Overdue by {days_overdue} days'
            else:
                days_remaining = (self.due_date - timezone.now().date()).days
                return f'Due in {days_remaining} days'
        else:
            if self.payment_date > self.due_date:
                days_late = (self.payment_date - self.due_date).days
                return f'Paid {days_late} days late'
            else:
                days_early = (self.due_date - self.payment_date).days
                return f'Paid {days_early} days early'

    status = models.CharField(
        max_length=10,
        choices=SaleStatus.CHOICES,
        default='pending'
    )

    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Sale {self.invoice_number} - {self.customer.name}"
