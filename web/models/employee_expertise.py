from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from web.models import Employee, ProductCategory


class EmployeeExpertise(models.Model):
    """Model for mapping employees to their product expertise areas"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    expertise_level = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    years_experience = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ['employee', 'category']