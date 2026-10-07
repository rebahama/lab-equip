from django.db import models
from django.contrib.auth.models import User
from equipment.models import Equipment


class Repair(models.Model):

    STATUS_CHOICES = [
        ("reported", "Reported"),
        ("in_progress", "In progress"),
        ("resolved", "Resolved"),
    ]

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    problem = models.TextField()

    repair_notes = models.TextField(blank=True, default="")

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="reported")

    reported_at = models.DateTimeField(auto_now_add=True)

    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.equipment} - {self.status}"
