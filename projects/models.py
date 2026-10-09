from django.db import models
from django.contrib.auth.models import User
from equipment.models import Equipment


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    equipment = models.ManyToManyField(Equipment, related_name="projects", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
