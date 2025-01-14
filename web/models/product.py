from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Sum, Avg, F

from web.models import ProductCategory
from web.models.sale_item import SaleItem


class Product(models.Model):
    """Model for products"""
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_level = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)

    def get_sales_trends(self, period_days=90):
        """Get sales trends for this product"""
        end_date = timezone.now()
        start_date = end_date - datetime.timedelta(days=period_days)

        return SaleItem.objects.filter(
            product=self,
            sale__date__range=[start_date, end_date],
            sale__status='completed'
        ).aggregate(
            total_quantity=Sum('quantity'),
            total_revenue=Sum(F('quantity') * F('unit_price')),
            avg_quantity_per_sale=Avg('quantity')
        )
