from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
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
