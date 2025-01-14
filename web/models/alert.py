from django.db import models
from django.utils import timezone

from web.config.constants import AlertTypes, AlertPriorities


class Alert(models.Model):
    """Model for system alerts and notifications"""
    type = models.CharField(max_length=20, choices=AlertTypes.CHOICES)
    priority = models.CharField(max_length=10, choices=AlertPriorities.CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey('Employee', on_delete=models.CASCADE)
    related_customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True)
    related_product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)

    def resolve(self, resolution_notes=None):
        """Mark alert as resolved"""
        self.resolved = True
        self.resolved_at = timezone.now()
        if resolution_notes:
            self.message += f"\n\nResolution: {resolution_notes}"
        self.save()

    def escalate(self):
        """Escalate alert priority"""
        priority_map = {
            'low': 'medium',
            'medium': 'high',
            'high': 'critical'
        }
        if self.priority in priority_map:
            self.priority = priority_map[self.priority]
            self.save()

    def send_notification(self):
        """Send notification based on alert type and priority"""
        if self.priority in ['high', 'critical']:
            # ارسال ایمیل فوری
            send_mail(
                f'هشدار مهم CRM: {self.get_type_display()}',
                self.message,
                'crm@company.com',
                [self.assigned_to.email],
                fail_silently=False,
            )

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['type', 'priority', 'resolved']),
            models.Index(fields=['assigned_to', 'resolved']),
        ]