from django.views.generic import CreateView, TemplateView, View
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from equipment.models import Equipment
from .models import Booking


class BookingCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
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

    def test_func(self):
        return self.request.user.groups.filter(name="Student").exists()

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
    TemplateView,
    LoginRequiredMixin,
    UserPassesTestMixin,
):

    model = Booking
    template_name = template_name = "booking/caretaker_manage_booking.html"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["bookings"] = Booking.objects.filter(
        approved=False
        )

        return context

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class ApproveBooking(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    Caretaker approves the booking, when booking is approved status changes
    to onloan on the Equipment object and chganges the relevant form fields.
    """

    model = Booking
    template_name = "booking/approve_booking.html"
    fields = ["approved"]

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

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

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class ManageBookingReturnsView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView,
):
    """
    Display booking returns waiting for caretaker confirmation.
    """

    template_name = "booking/view_student_return.html"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["bookings"] = Booking.objects.filter(
            returned=True,
            approved=True,
            active=True,
        )

        return context

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class ConfirmReturnBooking(
    LoginRequiredMixin,
    UserPassesTestMixin,
    View,
):
    """
    Caretaker confirms the return of equipment and field changes to avlaible
    """

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

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

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class ViewAllBookingCaretaker(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView):

    template_name = "booking/view_approved_history_caretaker.html"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )

class ShowActiveBookings(
    TemplateView,
    LoginRequiredMixin,
    UserPassesTestMixin,
):

    model = Booking
    template_name = template_name = "booking/caretaker_manage_booking.html"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["bookings"] = Booking.objects.filter(
        approved=True,
        active=True
        )

        return context

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class ShowHistoryReturnedBookingCaretaker(
    TemplateView,
    LoginRequiredMixin,
    UserPassesTestMixin,
):

    model = Booking
    template_name = template_name = "booking/caretaker_manage_booking.html"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["bookings"] = Booking.objects.filter(
        approved=True,
        active=False
        )

        return context

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )
