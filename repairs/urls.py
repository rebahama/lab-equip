from django.urls import path
from .views_student import CreateRepairFault


urlpatterns = [
    path("report/<int:equipment_id>", CreateRepairFault.as_view(), name="report-fault"),
    
]
