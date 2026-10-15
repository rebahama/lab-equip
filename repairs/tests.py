from django.urls import reverse
from equipment.tests import BaseEquipmentTestCase
from .models import Repair


class RepairReportTest(BaseEquipmentTestCase):
    def test_logged_out_user_cannot_create_repair(self):
        url = reverse("report-fault", args=[self.equipment.pk])
        response = self.client.post(
            url,
            data={"problem": "The equipment is not working."},
        )

        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_sends_repair(self):
        self.client.force_login(self.student)

        url = reverse("report-fault", args=[self.equipment.pk])

        response = self.client.post(
            url,
            data={"problem": "The equipment is not working."},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Repair.objects.filter(
                equipment=self.equipment,
                reported_by=self.student,
                problem="The equipment is not working.",
            ).exists()
        )

    def test_caretaker_receives_repair(self):
        self.client.force_login(self.caretaker)

        url = reverse("report-fault", args=[self.equipment.pk])

        response = self.client.post(
            url,
            data={"problem": "The equipment is not working."},
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Repair.objects.filter(
                equipment=self.equipment,
                reported_by=self.caretaker,
                problem="The equipment is not working.",
            ).exists()
        )
