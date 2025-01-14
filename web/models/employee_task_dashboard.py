from django.utils import timezone

from web.models.customer_follow_up import CustomerFollowUp


class EmployeeTaskDashboard:
    """Utility class for managing employee follow-up tasks"""

    @staticmethod
    def get_daily_tasks(employee):
        """Get daily task list for employee"""
        today = timezone.now().date()

        return {
            'urgent_follow_ups': CustomerFollowUp.objects.filter(
                assigned_to=employee,
                status='pending',
                priority='urgent',
                due_date__date=today
            ),
            'overdue_tasks': CustomerFollowUp.objects.filter(
                assigned_to=employee,
                status='pending',
                due_date__lt=timezone.now()
            ),
            'today_tasks': CustomerFollowUp.objects.filter(
                assigned_to=employee,
                status='pending',
                due_date__date=today
            ).exclude(priority='urgent'),
            'pending_alerts': Alert.objects.filter(
                assigned_to=employee,
                resolved=False
            ).order_by('-priority')
        }

    @staticmethod
    def generate_call_list(employee, date=None):
        """Generate prioritized call list for employee"""
        if date is None:
            date = timezone.now().date()

        tasks = CustomerFollowUp.objects.filter(
            assigned_to=employee,
            status='pending',
            due_date__date=date
        ).select_related('customer').order_by('-priority', 'due_date')

        return {
            'calls': [{
                'customer_name': task.customer.name,
                'phone_number': task.customer.phone,
                'priority': task.priority,
                'reason': task.notes,
                'best_time_to_call': task.customer.preferred_contact_time
            } for task in tasks],
            'total_calls': tasks.count(),
            'urgent_calls': tasks.filter(priority='urgent').count()
        }