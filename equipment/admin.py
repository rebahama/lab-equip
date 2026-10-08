from django.contrib import admin

from .models import Category, Equipment, EquipmentType, Location, EquipmentGuide


admin.site.register(Equipment)
admin.site.register(Category)
admin.site.register(EquipmentType)
admin.site.register(Location)
admin.site.register(EquipmentGuide)
