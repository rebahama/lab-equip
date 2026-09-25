from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Equipment, EquipmentType, Location


class CareTakerDashboard(TemplateView):
    template_name = "webpage/caretaker/caretaker_dashboard.html"


class EditEquipmentView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView,
):
    """
    Only the caretaker groups have access to the edit template, if student
    tries to access a forbidden page displays with no permission message.
    """

    model = Equipment
    template_name = "webpage/caretaker/edit_equipment.html"
    fields = [
        "equipment_type",
        "description",
        "serial_number",
        "location",
        "status",
        "condition",
        "image",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment_types"] = EquipmentType.objects.all()
        context["locations"] = Location.objects.all()

        return context

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, "Equipment updated successfully.", extra_tags="equipment"
        )

        return response

    def get_success_url(self):
        return f"/detail/{self.object.pk}/edit"

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )
