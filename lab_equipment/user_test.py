from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from equipment.models import Category, EquipmentType, Location, Equipment


User = get_user_model()


class BaseEquipmentTestCase(TestCase):
    def setUp(self):
        # Create groups
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

        categories = [
            ("Sensors", "Sensor equipment"),
            ("Cameras", "Cameras and webcams"),
            ("3D Printers", "3D printing equipment"),
            ("Microcontrollers", "Programmable microcontroller boards"),
            ("Raspberry Pi", "Single board computers"),
        ]

        self.category_objects = {}

        for name, description in categories:
            category, _ = Category.objects.get_or_create(
                name=name,
                defaults={"description": description},
            )
            self.category_objects[name] = category

        equipment_types = [
            ("Deltaco W-100", "Cameras", "A camera used for the web"),
            ("Prusa MINI+", "3D Printers", "Another type of 3D printer"),
            ("DHT22", "Sensors", "Temperature measurement kit"),
            ("Logitech C920", "Cameras", "USB HD webcam"),
            ("Prusa MK4", "3D Printers", "Compact 3D printer"),
            ("ESP32", "Microcontrollers", "ESP32 development boards"),
            ("Arduino Uno", "Microcontrollers", "Arduino Uno development board"),
            ("Raspberry Pi 4B", "Raspberry Pi", "Raspberry Pi 4 Model B"),
        ]

        for name, category_name, description in equipment_types:
            EquipmentType.objects.get_or_create(
                name=name,
                defaults={
                    "category": self.category_objects[category_name],
                    "description": description,
                },
            )

        locations = [
            "SHELF-A",
            "SHELF-B",
            "SHELF-C",
            "SHELF-D",
            "SHELF-E",
        ]

        self.location_objects = {}

        for name in locations:
            location, _ = Location.objects.get_or_create(name=name)
            self.location_objects[name] = location

        self.equipment = Equipment.objects.create(
            equipment_name="Raspberry Pi Test Unit",
            description="Test equipment for Django tests",
            serial_number="RPI-TEST-001",
            location=self.location_objects["SHELF-A"],
            status="available",
            condition="good",
            owner=self.caretaker,
        )
