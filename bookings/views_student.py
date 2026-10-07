from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from lab_equipment.mixin import StudentRequiredMixin
from .models import Booking


class ViewStudentBooking(
    StudentRequiredMixin,
    TemplateView,
):

    template_name = "booking/view_student_bookings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["active_bookings"] = Booking.objects.filter(
            student=self.request.user, active=True
        )

        return context


class ReturnBookingView(
    StudentRequiredMixin,
    View,
):
    def get(self, request, pk):

        booking = get_object_or_404(
            Booking,
            pk=pk,
            student=request.user,
            approved=True,
            returned=False,
            active=True,
        )

        return render(
            request,
            "booking/approve_return.html",
            {"booking": booking},
        )

    def post(self, request, pk):
        booking = get_object_or_404(
            Booking,
            pk=pk,
            student=request.user,
            approved=True,
            returned=False,
        )

        booking.returned = True
        booking.save()

        messages.success(
            request,
            "Request for return have been made, please come and leave your equipment at caretaker office.",
            extra_tags="booking",
        )

        return redirect("/bookings/show")


class ViewAllBookingStudent(StudentRequiredMixin, TemplateView):

    template_name = "booking/show_history_mybooking.html"


class ViewBookingHistory(
    StudentRequiredMixin,
    TemplateView,
):
    template_name = "booking/view_student_bookings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["active_bookings"] = Booking.objects.filter(
            student=self.request.user, active=False
        )

        return context
