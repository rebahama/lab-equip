from django.urls import path
from .views_student import CreateRepairFault
from .views_caretaker import (
ShowAllRepair,
ViewAllRepairsCareTaker,
StartRepair,
ViewActiveRepairs)


urlpatterns = [
    path("report/<int:equipment_id>", CreateRepairFault.as_view(), name="report-fault"),
    path("repair/showall", ShowAllRepair.as_view(), name="repair-show"),
    path("repair/showall/repairs", ViewAllRepairsCareTaker.as_view(), name="repair-show-all"),
    path("resolve/<int:pk>/", StartRepair.as_view(), name="start-repair"),
    path("repair/active/", ViewActiveRepairs.as_view(), name="active-repair"),
]
