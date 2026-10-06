from django.urls import path
from .views_student import CreateRepairFault
from .views_caretaker import ShowAllRepair


urlpatterns = [
    path("report/<int:equipment_id>", CreateRepairFault.as_view(), name="report-fault"),
    path("repair/showall", ShowAllRepair.as_view(), name="repair-show"),
]
