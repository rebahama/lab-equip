from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from equipment.models import Equipment


class Booking(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    student = models.ForeignKey(User, on_delete=models.CASCADE)

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    purpose = models.TextField()

    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):

        if self.start_time and self.end_time:

            if self.start_time >= self.end_time:

                raise ValidationError(
                    "The end time must be after the start time."
                )

    def __str__(self):
        return f"{self.student} - {self.equipment}"
