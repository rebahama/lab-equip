from django.db import models
from django.contrib.auth.models import User
from equipment.models import Equipment


class Booking(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    student = models.ForeignKey(User, on_delete=models.CASCADE)

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    purpose = models.TextField()

    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.equipment}"
