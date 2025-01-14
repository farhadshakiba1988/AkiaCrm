from django.contrib.auth.models import User
from django.db import models

from web.config.constants import ExpertiseLevels


class Employee(models.Model):
    """Model for managing sales employees/experts"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    mobile = models.CharField(max_length=11)
    home_phone = models.CharField(max_length=11, blank=True)
    address = models.TextField()
    position = models.CharField(max_length=100)
    join_date = models.DateField()
    profile_image = models.ImageField(upload_to='employees/', blank=True)
    linkedin_profile = models.URLField(blank=True)

    expertise_level = models.CharField(
        max_length=12,
        choices=ExpertiseLevels.CHOICES,
        default='beginner'
    )

    class Meta:
        ordering = ['user__last_name', 'user__first_name']

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"
