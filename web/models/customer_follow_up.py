from django.db import models
from django.utils import timezone
from web.config.constants import CustomerFollowUp


class CustomerFollowUp(models.Model):
    """Model for tracking customer follow-up tasks"""
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey('Employee', on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=CustomerFollowUp.PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=CustomerFollowUp.STATUS_CHOICES, default='pending')
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    contact_method = models.CharField(max_length=20, default='phone')  # phone, email, etc.

    def mark_completed(self, notes=None):
        self.status = 'completed'
        self.completed_at = timezone.now()
        if notes:
            self.notes = notes
        self.save()
