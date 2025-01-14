from django.db import models
from django.utils import timezone

from web.config.constants import CustomerTypes, StatusChoices
from django.db.models import Sum, Avg, Count, F

from web.models import Employee


class Customer(models.Model):
    """Model for managing customer companies"""
    name = models.CharField(max_length=200)
    economic_code = models.CharField(max_length=12, unique=True)
    registration_number = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_transaction_date = models.DateField(null=True, blank=True)
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    current_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    payment_terms = models.PositiveIntegerField(default=30)  # Days
    territory = models.ForeignKey('web.Territory', on_delete=models.SET_NULL, null=True)
    industry = models.CharField(max_length=100, blank=True)
    company_size = models.PositiveIntegerField(null=True, blank=True)
    annual_revenue = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def calculate_lifetime_value(self):
        """Calculate customer lifetime value"""
        total_sales = self.sale_set.filter(status='completed').aggregate(
            total=Sum('total_amount')
        )['total'] or 0

        years_active = (timezone.now().date() - self.created_at.date()).days / 365
        if years_active < 1:
            years_active = 1

        return total_sales / years_active

    def get_payment_history_metrics(self):
        """Get payment behavior metrics"""
        completed_sales = self.sale_set.filter(status='completed')
        total_sales = completed_sales.count()

        if total_sales == 0:
            return {
                'avg_payment_delay': 0,
                'on_time_payment_rate': 0,
                'total_sales': 0
            }

        on_time_payments = completed_sales.filter(
            payment_date__lte=F('due_date')
        ).count()

        avg_delay = completed_sales.filter(
            payment_date__gt=F('due_date')
        ).aggregate(
            avg_delay=Avg(F('payment_date') - F('due_date'))
        )['avg_delay']

        return {
            'avg_payment_delay': avg_delay.days if avg_delay else 0,
            'on_time_payment_rate': (on_time_payments / total_sales) * 100,
            'total_sales': total_sales
        }

    customer_type = models.CharField(
        max_length=10,
        choices=CustomerTypes.CHOICES,
        default=CustomerTypes.PRIVATE
    )

    # Customer status
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.CHOICES,
        default=StatusChoices.POTENTIAL
    )

    assigned_employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigned_customers'
    )

    def __str__(self):
        return self.name
