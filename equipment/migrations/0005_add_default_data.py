from django.db import migrations

def add_default_data(apps, schema_editor):
    Category = apps.get_model("equipment", "Category")
    EquipmentType = apps.get_model("equipment", "EquipmentType")
    Location = apps.get_model("equipment", "Location")
    Group = apps.get_model("auth", "Group")

    db = schema_editor.connection.alias

    Group.objects.using(db).get_or_create(name="Student")
    Group.objects.using(db).get_or_create(name="Caretaker")

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

class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0004_equipmentguide"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(add_default_data),
    ]
