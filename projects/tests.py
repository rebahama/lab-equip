from django.urls import reverse
from equipment.tests import BaseEquipmentTestCase
from projects.views import CreateProjectStudent
from unittest.mock import patch
from .models import Project


class ProjectTests(BaseEquipmentTestCase):
    def setUp(self):
        super().setUp()

        self.project = Project.objects.create(
            title="Existing project",
            description="A project for testing.",
            student=self.student,
        )

    def test_student_access_projects(self):
        self.client.force_login(self.student)

        response = self.client.get(reverse("my-projects"))

        self.assertEqual(response.status_code, 200)

    def test_student_creates_project(self):
        self.client.force_login(self.student)

        with patch.object(
            CreateProjectStudent,
            "get_success_url",
            return_value="/",
        ):
            self.client.post(
                reverse("create-project", args=[self.equipment.pk]),
                data={
                    "title": "Test project",
                    "description": "A project for testing.",
                },
            )

        self.assertTrue(
            Project.objects.filter(
                title="Test project",
                description="A project for testing.",
                student=self.student,
            ).exists()
        )

    def test_another_user_cannot_access_student_data(self):
        self.client.force_login(self.student2)

        response = self.client.get(reverse("show-projects", args=[self.project.pk]))

        self.assertEqual(response.status_code, 403)
