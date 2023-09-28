from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you need for user registration
    # Example:
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # Add custom related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # Custom related_name for groups
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # Custom related_name for user_permissions
        related_query_name='customuser'
    )


    def __str__(self):
        return self.username
