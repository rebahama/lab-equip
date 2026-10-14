from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from .models import Equipment


class EquipmentViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="student",
            password="testpassword123"
        )
        self.client.login(
            username="student",
            password="testpassword123"
        )

    def test_view_equipment_page(self):
        response = self.client.get(reverse("show-student"))

        self.assertEqual(response.status_code, 200)


class CaretakerDashboardTests(TestCase):

    def setUp(self):
        self.student_group, _ = Group.objects.get_or_create(
            name="Student"
        )
        self.caretaker_group, _ = Group.objects.get_or_create(
            name="Caretaker"
        )

        User = get_user_model()
        self.student = User.objects.create_user(
            username="student",
            password="testpassword123"
        )
        self.student.groups.add(self.student_group)

    def test_student_cannot_access_caretaker_dashboard(self):
        self.client.force_login(self.student)

        response = self.client.get(
            reverse("show-dashboard")
        )

        self.assertEqual(response.status_code, 403)