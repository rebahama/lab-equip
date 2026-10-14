from django.urls import reverse
from lab_equipment.user_test import BaseEquipmentTestCase


class EquipmentViewTests(BaseEquipmentTestCase):
    def test_view_equipment_page(self):
        self.client.force_login(self.student)

        response = self.client.get(reverse("show-student"))

        self.assertEqual(response.status_code, 200)


class CaretakerDashboardTests(BaseEquipmentTestCase):
    def test_student_cannot_access_caretaker_dashboard(self):
        self.client.force_login(self.student)

        response = self.client.get(reverse("show-dashboard"))

        self.assertEqual(response.status_code, 403)


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
