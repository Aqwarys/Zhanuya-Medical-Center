from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Пример: Student, Professor, etc.

    def __str__(self):
        return f'{self.name}'


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Пример: Computer Science, Biology, etc.

    def __str__(self):
        return f'{self.name}'

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Номер телефона
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True, null=True)  # Пол
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)  # Роль пользователя

    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"
