# constants.py

class ExpertiseLevels:
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    EXPERT = 'expert'

    CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (EXPERT, 'Expert')
    ]


# constants.py

class CustomerTypes:
    GOVERNMENT = 'government'
    PRIVATE = 'private'
    INDIVIDUAL = 'individual'

    CHOICES = [
        (GOVERNMENT, 'Government'),
        (PRIVATE, 'Private Company'),
        (INDIVIDUAL, 'Individual')
    ]


class StatusChoices:
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    POTENTIAL = 'potential'

    CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (POTENTIAL, 'Potential')
    ]


class InteractionTypes:
    CALL = 'call'
    MEETING = 'meeting'
    EMAIL = 'email'
    PROPOSAL = 'proposal'

    CHOICES = [
        (CALL, 'Phone Call'),
        (MEETING, 'Meeting'),
        (EMAIL, 'Email'),
        (PROPOSAL, 'Proposal Submission')
    ]


class SaleStatus:
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

    CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled')
    ]


class CustomerFollowUp:
    """Model for tracking customer follow-up tasks"""
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    URGENT = 'urgent'

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (URGENT, 'Urgent')
    ],

    PENDING = 'pending'
    IN_PROGRESS = 'in progress'
    COMPLETED = 'completed'
    FAILED = 'failed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed')
    ]


class Alert:

    STOCK = 'stock'
    PAYMENT = 'payment'
    SALES = 'sales'
    CUSTOMER = 'customer'
    PRICE = 'price'
    FOLLOW_UP = 'follow_up'
    SYSTEM = 'system'

    ALERT_TYPES_CHOICES = [
        ('STOCK', 'موجودی کم'),
        ('PAYMENT', 'پرداخت دیرکرد'),
        ('SALES', 'هدف فروش'),
        ('CUSTOMER', 'فعالیت مشتری'),
        ('PRICE', 'تغییر قیمت'),
        ('FOLLOW_UP', 'پیگیری'),
        ('SYSTEM', 'سیستمی')
    ],

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    CRITICAL = 'critical'

    PRIORITY_LEVELS_CHOICES = [
        ('LOW', 'کم'),
        ('MEDIUM', 'متوسط'),
        ('HIGH', 'زیاد'),
        ('CRITICAL', 'بحرانی')
    ]
