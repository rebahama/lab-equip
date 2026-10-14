from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model


User = get_user_model()


class BaseEquipmentTestCase(TestCase):
    def setUp(self):
        self.student_group, _ = Group.objects.get_or_create(name="Student")
        self.caretaker_group, _ = Group.objects.get_or_create(name="Caretaker")

        self.student = User.objects.create_user(
            username="student",
            password="testpassword123",
        )
        self.student.groups.add(self.student_group)

        self.caretaker = User.objects.create_user(
            username="caretaker",
            password="testpassword123",
        )
        self.caretaker.groups.add(self.caretaker_group)
