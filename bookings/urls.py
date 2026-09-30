from django.urls import path
from .views_caretaker import (
    BookingCreateView,
    ShowAllBookingView,
    ApproveBooking,
    ManageBookingReturnsView,
    ConfirmReturnBooking,
)
from .views_student import ViewStudentBooking, ReturnBookingView

urlpatterns = [
    path(
        "booking/<int:equipment_id>", BookingCreateView.as_view(), name="create-booking"
    ),
    path("booking/caretaker", ShowAllBookingView.as_view(), name="manage-booking"),
    path("booking/<int:pk>/approve", ApproveBooking.as_view(), name="approve-booking"),
    path("bookings/show", ViewStudentBooking.as_view(), name="student-booking"),
    path("return/<int:pk>/", ReturnBookingView.as_view(), name="return-booking"),
    path("booking/returns", ManageBookingReturnsView.as_view(), name="manage-returns"),
    path("booking/returns/<int:pk>/confirm/", ConfirmReturnBooking.as_view(), name="confirm-return"),
]
