from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Booking
from equipment.models import Equipment


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
