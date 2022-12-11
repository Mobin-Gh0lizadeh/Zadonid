from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_Seller = models.BooleanField('Seller status', default=False)
    is_Customer = models.BooleanField('Customer status', default=False)
    phone = models.PositiveIntegerField(null=True, blank=True)
    job = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.username}'

