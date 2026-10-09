from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from lab_equipment.mixin import StudentRequiredMixin
from equipment.models import Equipment
from .models import Project


class CreateProjectStudent(StudentRequiredMixin, CreateView):

    model = Project
    template_name = "projects/create_project.html"
    fields = ["title", "description"]

    def get_success_url(self):
        return reverse("create-project", kwargs={"pk": self.kwargs["pk"]})

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

    # success_url = reverse_lazy("show-projects")
