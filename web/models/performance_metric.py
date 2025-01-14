from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from web.models import Employee


class PerformanceMetric(models.Model):
    """Model for tracking employee performance metrics"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    period_start = models.DateField()
    period_end = models.DateField()
    sales_target = models.DecimalField(max_digits=12, decimal_places=2)
    sales_achieved = models.DecimalField(max_digits=12, decimal_places=2)
    new_customers = models.PositiveIntegerField()
    customer_retention_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        unique_together = ['employee', 'period_start', 'period_end']
