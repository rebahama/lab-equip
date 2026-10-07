from django.views.generic import CreateView, TemplateView, View
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from lab_equipment.mixin import CaretakerRequiredMixin, StudentRequiredMixin
from equipment.models import Equipment
from .models import Booking


class BookingCreateView(
    StudentRequiredMixin,
    CreateView,
):
    """
    Only the students can make a booking, caretaker have
    to approve the form field "approve". To true if booking
    is valid.
    """

    template_name = "booking/booking_form.html"

    model = Booking

    fields = [
        "start_time",
        "end_time",
        "purpose",
    ]

    def get_success_url(self):
        return f"/detail/{self.kwargs['equipment_id']}"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment"] = Equipment.objects.get(pk=self.kwargs["equipment_id"])

        return context

    def form_valid(self, form):

        equipment = Equipment.objects.get(pk=self.kwargs["equipment_id"])

        form.instance.equipment = equipment
        form.instance.student = self.request.user
        form.instance.approved = False

        messages.success(
            self.request,
            "Booking request sent. Please wait for confirmation from caretaker.",
            extra_tags="booking",
        )

        return super().form_valid(form)


class ShowAllBookingView(
    CaretakerRequiredMixin,
    TemplateView,
):

    model = Booking
    template_name = template_name = "booking/caretaker_manage_booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["bookings"] = Booking.objects.filter(approved=False)

        return context


class ApproveBooking(CaretakerRequiredMixin, View):
    """
    Caretaker approves the booking, when booking is approved status changes
    to onloan on the Equipment object and chganges the relevant form fields.
    """

    model = Booking
    template_name = "booking/approve_booking.html"
    fields = ["approved"]

    def get(self, request, pk):

        booking = Booking.objects.get(pk=pk)

        return render(
            request,
            "booking/approve_booking.html",
            {"booking": booking},
        )

    def post(self, request, pk):

        booking = Booking.objects.get(pk=pk)

        booking.approved = True
        booking.save()

        equipment = booking.equipment
        equipment.status = "on_loan"
        equipment.save()

        messages.success(
            request,
            "Booking has been approved and confirmed",
            extra_tags="approved",
        )

        return redirect("/booking/caretaker")


class ManageBookingReturnsView(
    CaretakerRequiredMixin,
    TemplateView,
):
    """
    Display booking returns waiting for caretaker confirmation.
    """

    template_name = "booking/view_student_return.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["bookings"] = Booking.objects.filter(
            returned=True,
            approved=True,
            active=True,
        )

        return context


class ConfirmReturnBooking(
    CaretakerRequiredMixin,
    View,
):
    """
    Caretaker confirms the return of equipment and field changes to avlaible
    """

    def post(self, request, pk):

        booking = get_object_or_404(
            Booking,
            pk=pk,
            returned=True,
            active=True,
        )

        booking.active = False
        booking.save()

        equipment = booking.equipment
        equipment.status = request.POST.get("status")
        equipment.save()

        messages.success(
            request,
            "Equipment return has been confirmed.",
            extra_tags="returned",
        )

        return redirect("manage-returns")


class ViewAllBookingCaretaker(CaretakerRequiredMixin, TemplateView):

    template_name = "booking/view_approved_history_caretaker.html"


class ShowActiveBookings(
    CaretakerRequiredMixin,
    TemplateView,
):

    model = Booking
    template_name = template_name = "booking/caretaker_manage_booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["bookings"] = Booking.objects.filter(approved=True, active=True)

        return context


class ShowHistoryReturnedBookingCaretaker(
    CaretakerRequiredMixin,
    TemplateView,
):

    model = Booking
    template_name = template_name = "booking/caretaker_manage_booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["bookings"] = Booking.objects.filter(approved=True, active=False)

        return context
