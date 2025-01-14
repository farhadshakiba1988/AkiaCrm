from django.db import models
from django.utils import timezone

from web.config.constants import InteractionTypes
from web.models import Customer, Employee


class CustomerInteraction(models.Model):
    """Model for tracking interactions with customers"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    interaction_type = models.CharField(
        max_length=10,
        choices=InteractionTypes.CHOICES
    )

    notes = models.TextField()
    follow_up_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
