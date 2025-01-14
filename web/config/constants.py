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
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
