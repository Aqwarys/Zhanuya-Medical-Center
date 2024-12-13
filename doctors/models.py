from django.db import models

# Create your models here.
class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('dermatology', 'Dermatology'),
        ('pediatrics', 'Pediatrics'),
        ('orthopedics', 'Orthopedics'),
        ('general', 'General Practice'),
    ]

    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    biography = models.TextField(blank=True, null=True)
    available_days = models.CharField(max_length=255, blank=True, null=True)
    experience = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.full_name}'