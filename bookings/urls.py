from django.urls import path
from .views import (
    BookingCreateView,
    ShowAllBookingView,
    ApproveBooking
)

urlpatterns = [
    path("booking/<int:equipment_id>", BookingCreateView.as_view(), name="create-booking"),
    path("booking/caretaker", ShowAllBookingView.as_view(), name="manage-booking"),
    path("booking/<int:pk>/approve", ApproveBooking.as_view(), name="approve-booking"),
]
