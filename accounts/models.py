from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_USER = 'user'
    ROLE_STAFF = 'staff'
    ROLE_ADMIN = 'admin'
    
    ROLE_CHOICES = [
        (ROLE_USER, 'Regular User'),
        (ROLE_STAFF, 'Library Staff'),
        (ROLE_ADMIN, 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ROLE_USER)
    
    @property
    def is_library_staff(self):
        return self.role in [self.ROLE_STAFF, self.ROLE_ADMIN]
    
    @property
    def is_library_admin(self):
        return self.role == self.ROLE_ADMIN
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
