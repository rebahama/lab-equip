from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Equipment, EquipmentType, Location, Category


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
        "equipment_name",
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


class DeleteEquipmentView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
):
    """
    Only the caretaker groups have access to the delete template, if student
    tries to access a forbidden page displays with no permission message.
    """

    model = Equipment
    template_name = "webpage/caretaker/delete_equipment.html"
    success_url = reverse_lazy("show-student")

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def form_valid(self, form):
        messages.success(
            self.request, "Equipment deleted successfully.", extra_tags="equipment"
        )

        return super().form_valid(form)

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class EditCategoryPage(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView,
):
    """
    Only the caretaker groups have access to the edit category.
    """

    fields = ["name"]

    model = Category
    template_name = "webpage/caretaker/caretaker_edit_category.html"
    categories = Category.objects.all()

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()

        return context

    def get_success_url(self):
        return f"/category/{self.object.pk}/edit"

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )

    def form_valid(self, form):
        messages.success(
            self.request, "Category changed successfully.", extra_tags="category"
        )

        return super().form_valid(form)


class EditEquipmentType(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView,
):
    """
    Only the caretaker groups have access to the edit equipment type page.
    """

    fields = ["name", "description"]

    model = EquipmentType
    template_name = "webpage/caretaker/caretaker_edit_equipment_type.html"
    context_object_name = "equipment_type"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment_types"] = EquipmentType.objects.all()

        return context

    def get_success_url(self):
        return self.request.path

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )

    def form_valid(self, form):
        messages.success(
            self.request,
            "Equipment type was changed successfully.",
            extra_tags="equipment-type",
        )

        return super().form_valid(form)
