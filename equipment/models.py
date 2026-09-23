from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):

    STATUS_CHOICES = [
        ("available", "Available"),
        ("on_loan", "On loan"),
        ("in_repair", "In repair"),
        ("out_of_service", "Out of service"),
        ("retired", "Retired"),
    ]

    CONDITION_CHOICES = [
        ("excellent", "Excellent"),
        ("good", "Good"),
        ("fair", "Fair"),
        ("poor", "Poor"),
        ("damaged", "Damaged"),
    ]

    name = models.CharField(max_length=200)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    description = models.TextField(blank=True)
    serial_number = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="available"
    )

    condition = models.CharField(
        max_length=20, choices=CONDITION_CHOICES, default="good"
    )

    image = models.ImageField(upload_to="equipment/images/", blank=True, null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
