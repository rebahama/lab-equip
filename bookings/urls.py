from django.urls import path
from .views import (
    BookingCreateView,

)

urlpatterns = [
    path("booking/<int:equipment_id>", BookingCreateView.as_view(), name="create-booking"),

]
