from django.views.generic import CreateView, ListView, TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from lab_equipment.mixin import StudentRequiredMixin
from equipment.models import Equipment, EquipmentType
from .models import Project


class CreateProjectStudent(StudentRequiredMixin, CreateView):

    model = Project
    template_name = "projects/create_project.html"
    fields = ["title", "description"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment"] = Equipment.objects.get(id=self.kwargs["pk"])

        return context

    def form_valid(self, form):
        form.instance.student = self.request.user
        equipment = get_object_or_404(Equipment, pk=self.kwargs["pk"])
        response = super().form_valid(form)
        self.object.equipment.add(equipment)
        messages.success(self.request, "Project created successfully!")
        return response

    def get_success_url(self):
        equipment = get_object_or_404(Equipment, pk=self.kwargs["pk"])

        return reverse_lazy("show-projects", kwargs={"pk": equipment.equipment_type_id})


class ViewCreatedProject(StudentRequiredMixin, TemplateView):
    template_name = "projects/view_projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        equipment_type = get_object_or_404(EquipmentType, id=self.kwargs["pk"])

        context["equipment_type"] = equipment_type
        context["projects"] = Project.objects.filter(
            equipment__equipment_type=equipment_type, student=self.request.user
        ).distinct()

        return context
