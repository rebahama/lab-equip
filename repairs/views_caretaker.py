from django.views.generic import TemplateView, View, ListView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from lab_equipment.mixin import CaretakerRequiredMixin
from .models import Repair


class ShowAllRepair(CaretakerRequiredMixin, TemplateView):

    template_name = "repairs/show-active-history-repairs.html"


class ViewAllRepairsCareTaker(CaretakerRequiredMixin, ListView):
    
    model = Repair
    template_name = "repairs/show-active-faults.html"
    context_object_name = "repairs"

    def get_queryset(self):
        return Repair.objects.filter(status="reported")


class StartRepair(CaretakerRequiredMixin, View):
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


class ViewActiveRepairs(CaretakerRequiredMixin, ListView):

    model = Repair
    template_name = "repairs/display-inprogress-repairs.html"
    context_object_name = "active_repairs"

    def get_queryset(self):
        return Repair.objects.filter(status="in_progress")


class FinishRepair(CaretakerRequiredMixin, View):
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


class ResolvedRepairs(CaretakerRequiredMixin, ListView):
    
    model = Repair
    template_name = "repairs/resloved-repairs.html"
    context_object_name = "resolved_repairs"

    def get_queryset(self):
        return Repair.objects.filter(status="resolved")
