from django.db import models


class ProductCategory(models.Model):
    """Model for product categories"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )

    class Meta:
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name