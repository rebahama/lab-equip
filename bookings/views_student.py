from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Booking


class ViewStudentBooking(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView,
):

    template_name = "booking/view_student_bookings.html"

    def test_func(self):
        return self.request.user.groups.filter(name="Student").exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["bookings"] = Booking.objects.filter(student=self.request.user)

        return context

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class ReturnBookingView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    View,
):
    def test_func(self):
        return self.request.user.groups.filter(
            name="Student"
        ).exists()

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

    def handle_no_permission(self):
        return TemplateView.as_view(
            template_name="webpage/no_permission.html"
        )(self.request)
