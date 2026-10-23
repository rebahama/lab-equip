from django.db import migrations
from django.contrib.auth.hashers import make_password


def add_default_data(apps, schema_editor):
    Category = apps.get_model("equipment", "Category")
    EquipmentType = apps.get_model("equipment", "EquipmentType")
    Equipment = apps.get_model("equipment", "Equipment")
    Location = apps.get_model("equipment", "Location")
    Group = apps.get_model("auth", "Group")
    User = apps.get_model("auth", "User")

    db = schema_editor.connection.alias

    Group.objects.using(db).get_or_create(name="Student")
    caretaker_group, _ = Group.objects.using(db).get_or_create(name="Caretaker")

    test_user, created = User.objects.using(db).get_or_create(
    username="testcaretaker",
    defaults={
        "is_active": True,
        "password": make_password("Testing"),
    },
)


    test_user.groups.add(caretaker_group)

    categories = [
        ("Sensors", "Sensor equipment"),
        ("Cameras", "Cameras and webcams"),
        ("3D Printers", "3D printing equipment"),
        ("Microcontrollers", "Programmable microcontroller boards"),
        ("Raspberry Pi", "Single board computers"),
    ]

    category_objects = {}

    for name, description in categories:
        category, _ = Category.objects.using(db).get_or_create(
            name=name,
            defaults={"description": description},
        )
        category_objects[name] = category

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
        EquipmentType.objects.using(db).get_or_create(
            name=name,
            defaults={
                "category_id": category_objects[category_name].pk,
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

    for name in locations:
        Location.objects.using(db).get_or_create(name=name)

    equipment_data = [

        (
            "Raspberry-01",
            "Used for computers",
            "RP-01",
            "Raspberry Pi 4B",
            "SHELF-A",
            "good",
            "available",
        ),
        (
            "Raspberry-02",
            "Used for computers",
            "RP-02",
            "Raspberry Pi 4B",
            "SHELF-A",
            "good",
            "available",
        ),
        # ESP32
        (
            "ESP 32-01",
            "A good microcontroller aasasasa",
            "M-01",
            "ESP32",
            "SHELF-B",
            "excellent",
            "available",
        ),
        (
            "ESP 32-02",
            "ESP32-S, a good example",
            "M-02",
            "ESP32",
            "SHELF-B",
            "excellent",
            "on_loan",
        ),

        (
            "Prusa MK4-01",
            "Used for tech",
            "PR-01",
            "Prusa MK4",
            "SHELF-C",
            "good",
            "on_loan",
        ),

        (
            "Prusa MINI+-01",
            "a good example",
            "PR-PLUS-01",
            "Prusa MINI+",
            "SHELF-E",
            "good",
            "available",
        ),
    ]

    for (
        name,
        description,
        serial,
        type_name,
        location_name,
        condition,
        status,
    ) in equipment_data:
        equipment_type = EquipmentType.objects.using(db).get(name=type_name)
        location = Location.objects.using(db).get(name=location_name)

        Equipment.objects.using(db).get_or_create(
            serial_number=serial,
            defaults={
                "equipment_type_id": equipment_type.pk,
                "equipment_name": name,
                "description": description,
                "location_id": location.pk,
                "status": status,
                "condition": condition,
                "owner_id": test_user.pk,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0004_equipmentguide"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(add_default_data),
    ]
