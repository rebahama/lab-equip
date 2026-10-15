from django.urls import reverse
from lab_equipment.user_test import BaseEquipmentTestCase
from .models import EquipmentGuide, EquipmentType


class EquipmentViewTests(BaseEquipmentTestCase):
    def test_view_equipment_page(self):
        self.client.force_login(self.student)

        response = self.client.get(reverse("show-student"))

        self.assertEqual(response.status_code, 200)


class CaretakerDashboardTests(BaseEquipmentTestCase):
    def setUp(self):
        super().setUp()

        self.equipment_type = EquipmentType.objects.get(name="Raspberry Pi 4B")

    def test_student_cannot_access_caretaker_dashboard(self):
        self.client.force_login(self.student)

        response = self.client.get(reverse("show-dashboard"))

        self.assertEqual(response.status_code, 403)

    def test_caretaker_creates_guide(self):
        self.client.force_login(self.caretaker)

        url = reverse("create-guide", args=[self.equipment_type.pk])

        response = self.client.post(
            url,
            data={
                "title": "testing",
                "content": "this is guide content",
            },
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            EquipmentGuide.objects.filter(
                equipment_type=self.equipment_type,
                title="testing",
                content="this is guide content",
            ).exists()
        )


class CaretakerAcessStudentPage(BaseEquipmentTestCase):
    def test_caretaker_access_student(self):
        self.client.force_login(self.caretaker)

        response = self.client.get(reverse("my-projects"))

        self.assertEqual(response.status_code, 403)


class NotLoggedInUser(BaseEquipmentTestCase):
    def test_guest_cannot_access_caretaker_dashboard(self):
        response = self.client.get(reverse("show-dashboard"))

        self.assertEqual(response.status_code, 403)

    def test_guest_cannot_create_equipment(self):
        response = self.client.get(reverse("create"))
        self.assertEqual(response.status_code, 403)
