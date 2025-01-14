from django.db import models


class Territory(models.Model):
    """Model for managing sales territories"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=100)
    potential_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)