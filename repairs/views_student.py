from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from equipment.models import Equipment
from .models import Repair


class CreateRepairFault(LoginRequiredMixin, CreateView):

    model = Repair
    template_name = "repairs/report-fault.html"
    fields = [
        "problem",
    ]

    def form_valid(self, form):
        form.instance.equipment = get_object_or_404(
            Equipment, pk=self.kwargs["equipment_id"]
        )

        form.instance.reported_by = self.request.user

        messages.success(
            self.request,
            "Fault has been reported successfully.",
            extra_tags="repair",
        )

        return super().form_valid(form)

    def get_success_url(self):
        return f"/detail/{self.kwargs['equipment_id']}"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment"] = get_object_or_404(
            Equipment, pk=self.kwargs["equipment_id"]
        )

        return context

    def handle_no_permission(self):
        return render(
            self.request,
            "webpage/no_permission.html",
            status=403,
        )
