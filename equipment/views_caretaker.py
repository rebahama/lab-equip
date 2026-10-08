from django.views.generic import UpdateView, DeleteView, TemplateView, ListView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from lab_equipment.mixin import CaretakerRequiredMixin
from .models import Equipment, EquipmentType, Location, Category, EquipmentGuide


class CareTakerDashboard(
CaretakerRequiredMixin,
TemplateView):

    template_name = "webpage/caretaker/caretaker_dashboard.html"


class EditEquipmentView(
    CaretakerRequiredMixin,
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

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.object.status in ["retired"]:
            messages.success(
                self.request,
                "Equipment is no longer active because it has been retired" \
                " You can find it in dashboard on the archive equipment page.",
                extra_tags="equipment",
            )

        else:
            messages.success(
                self.request,
                "Equipment updated successfully.",
                extra_tags="equipment",
            )

        return response

    def get_success_url(self):
        return f"/detail/{self.object.pk}/edit"


class DeleteEquipmentView(
    CaretakerRequiredMixin,
    DeleteView,
):
    """
    Only the caretaker groups have access to the delete template, if student
    tries to access a forbidden page displays with no permission message.
    """

    model = Equipment
    template_name = "webpage/caretaker/delete_equipment.html"
    success_url = reverse_lazy("show-student")

    def form_valid(self, form):
        messages.success(
            self.request, "Equipment deleted successfully.", extra_tags="equipment"
        )

        return super().form_valid(form)


class EditCategoryPage(
    CaretakerRequiredMixin,
    UpdateView,
):
    """
    Only the caretaker groups have access to the edit category.
    """

    fields = ["name", "description"]

    model = Category
    template_name = "webpage/caretaker/caretaker_edit_category.html"
    categories = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()

        return context

    def get_success_url(self):
        return f"/category/{self.object.pk}/edit"

    def form_valid(self, form):
        messages.success(
            self.request, "Category changed successfully.", extra_tags="category"
        )

        return super().form_valid(form)


class EditEquipmentType(
    CaretakerRequiredMixin,
    UpdateView,
):
    """
    Only the caretaker groups have access to the edit equipment type page.
    """

    fields = ["name", "description"]

    model = EquipmentType
    template_name = "webpage/caretaker/caretaker_edit_equipment_type.html"
    context_object_name = "equipment_type"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment_types"] = EquipmentType.objects.all()

        return context

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        messages.success(
            self.request,
            "Equipment type was changed successfully.",
            extra_tags="equipment-type",
        )

        return super().form_valid(form)


class ViewNotInServiceEquipment(
    CaretakerRequiredMixin,
    ListView
):

    model = Equipment
    template_name = "webpage/caretaker/not-in-service.html"
    context_object_name = "equipment"

    def get_queryset(self):
        return Equipment.objects.filter(status__in=["out_of_service", "retired"])


class CreateEquipmentGuide(
    CaretakerRequiredMixin,
    CreateView
):

    model = EquipmentGuide
    template_name = "webpage/forms/create_equipment_guides.html"
    fields = [
        "title",
        "content",
    ]

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["equipment_type"] = EquipmentType.objects.get(id=self.kwargs["pk"])
        return context

    def form_valid(self, form):

        form.instance.equipment_type = EquipmentType.objects.get(id=self.kwargs["pk"])
        form.instance.created_by = self.request.user

        response = super().form_valid(form)

        messages.success(
            self.request,
            "Equipment guide was created successfully.",
            extra_tags="equipment",
        )

        return response

    def get_success_url(self):
        return reverse("view-guide-all", args=[self.kwargs["pk"]])
