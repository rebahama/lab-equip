from django.views.generic import TemplateView, View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Repair


class ShowAllRepair(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = "repairs/show-active-history-repairs.html"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class ViewAllRepairsCareTaker(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    model = Repair
    template_name = "repairs/show-active-faults.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["repairs"] = Repair.objects.filter(status__in=["reported"])

        return context

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class StartRepair(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )

    def post(self, request, pk):
        repair = get_object_or_404(Repair, pk=pk)

        repair.status = "in_progress"
        repair.save()

        equipment = repair.equipment
        equipment.status = "in_repair"
        equipment.save()

        messages.success(
            request,
            "Repair has been succesfully added to in active repairs.",
            extra_tags="repair",
        )

        return redirect("/repair/showall/repairs")


class ViewActiveRepairs(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "repairs/display-inprogress-repairs.html"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["active_repairs"] = Repair.objects.filter(status="in_progress")

        return context


class FinishRepair(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )

    def post(self, request, pk):
        repair = get_object_or_404(Repair, pk=pk)

        equipment = repair.equipment
        equipment.status = "available"
        equipment.save()

        repair.status = "resolved"
        repair.save()

        messages.success(
            request,
            "Repair has been successfully repaired and available again",
            extra_tags="available",
        )

        return redirect("/repair/active")
