from django.urls import reverse
from equipment.tests import BaseEquipmentTestCase
from .models import Booking


class BookingTest(BaseEquipmentTestCase):
    def test_student_creates_booking(self):
        self.client.force_login(self.student)

        url = reverse("create-booking", args=[self.equipment.pk])

        response = self.client.post(
            url,
            data={
                "start_time": "2026-10-20T10:00",
                "end_time": "2026-10-20T12:00",
                "purpose": "Course project",
            },
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Booking.objects.filter(
                equipment=self.equipment,
                student=self.student,
                purpose="Course project",
            ).exists()
        )

    def test_wrong_date(self):
        self.client.force_login(self.student)

        url = reverse("create-booking", args=[self.equipment.pk])

        response = self.client.post(
            url,
            data={
                "start_time": "2026-10-19T10:00",
                "end_time": "2026-10-17T12:00",
                "purpose": "Course project",
            },
        )

        self.assertEqual(response.status_code, 200)

        self.assertFalse(
            Booking.objects.filter(
                equipment=self.equipment,
                student=self.student,
                purpose="Course project",
            ).exists()
        )

    def test_guest_cannot_access_booking(self):
        response = self.client.get(reverse("create-booking", args=[self.equipment.pk]))

        self.assertEqual(response.status_code, 403)
