from django.db import models

# Create your models here.
class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)  # Сообщение необязательно

    def __str__(self):
        return f"Appointment with {self.full_name} on {self.date} at {self.time}"