from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from lab_equipment.mixin import CaretakerRequiredMixin
from bookings.models import Booking
from repairs.models import EquipmentProblem
from .models import Equipment, Category, EquipmentType, Location, EquipmentGuide


class CreatePageCaretakerView(
    CaretakerRequiredMixin,
    CreateView,
):
    """
    Only the caretaker groups have access to the create template, if student
    tries to access a forbidden page displays with no permission message.
    """

    model = Equipment
    template_name = "webpage/caretaker/create_caretaker.html"
    fields = [
        "equipment_type",
        "equipment_name",
        "description",
        "serial_number",
        "location",
        "status",
        "condition",
        "image",
    ]

    def get_success_url(self):
        return reverse(
            "show-detail",
            kwargs={"pk": self.object.pk}
        )

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)

        messages.success(
            self.request,
            f'Equipment "{self.object.equipment_name}" was successfully created. '
            f'<a href="{reverse("show-detail", kwargs={"pk": self.object.pk})}">'
            f'View equipment</a>',
            extra_tags="equipment",
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()
        context["equipment_types"] = EquipmentType.objects.all()
        context["locations"] = Location.objects.all()

        return context


class ViewAllStudent(LoginRequiredMixin, TemplateView):
    """Display all equipment to users, if search word contains
    Equipment name, serial number or type the quearry will be displayed
    Also Filtering based on the status.
    If a equipment is boked then let the user
    find the same type with the equipment type
    field.
    """

    model = Equipment
    template_name = "webpage/student/view_all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get("q")
        status = self.request.GET.get("status")
        category = self.request.GET.get("category")
        equipment_type = self.request.GET.get("equipment_type")

        equipment = Equipment.objects.filter(
        status__in=["available", "on_loan", "in_repair","out_of_service"]
        ).order_by("-created_at")

        if query:
            equipment = equipment.filter(
                Q(equipment_name__icontains=query)
                | Q(serial_number__icontains=query)
                | Q(equipment_type__name__icontains=query)
                | Q(equipment_type__category__name__icontains=query)
            )

        if equipment_type:
            equipment = equipment.filter(equipment_type_id=equipment_type)

        if status:
            equipment = equipment.filter(status=status)

        if category:
            equipment = equipment.filter(equipment_type__category__name=category)

        context["equipment"] = equipment

        return context


class ViewAllDetailPage(LoginRequiredMixin, DetailView):
    """Display the detailed page when clicking view more"""

    model = Equipment
    template_name = "webpage/student/view_detail.html"
    context_object_name = "equipment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        equipment_queryset = Equipment.objects.filter(
            equipment_type=self.object.equipment_type
        )

        context["available_count"] = equipment_queryset.filter(
            status="available"
        ).count()

        context["on_loan_count"] = equipment_queryset.filter(status="on_loan").count()

        context["total_count"] = equipment_queryset.exclude(
            status__in=["retired","out_of_service"]
        ).count()

        pending_booking = Booking.objects.filter(
            equipment=self.object, active=True, approved=False
        ).exists()

        context["known_problems"] = EquipmentProblem.objects.filter(
            equipment_type=self.object.equipment_type
        )

        context["pending_booking"] = pending_booking

        return context


class ViewCategoryPage(LoginRequiredMixin, TemplateView):
    """Display the categories and display the counts inside the categories"""

    model = Category
    template_name = "webpage/caretaker/category_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()

        for category in categories:
            category.equipment_count = Equipment.objects.filter(
                equipment_type__category=category
            ).count()

            category.equipment_type_count = EquipmentType.objects.filter(
                category=category
            ).count()

        context["categories"] = categories

        return context


class ViewCategoryDetailPage(LoginRequiredMixin, DetailView):
    """Display the only the specfik categories that was clicked on"""

    model = Category
    template_name = "webpage/caretaker/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment_types"] = EquipmentType.objects.filter(category=self.object)

        context["equipment_count"] = Equipment.objects.filter(
            equipment_type__category=self.object
        ).count()

        for equipment_type in context["equipment_types"]:
            equipment_type.equipment_count = Equipment.objects.filter(
                equipment_type=equipment_type
            ).count()

        return context

class ViewEquipmentTypeDetailPage(LoginRequiredMixin, DetailView):

    model = EquipmentType
    template_name = "webpage/caretaker/equipment_type_detail.html"
    context_object_name = "equipment_type"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment"] = Equipment.objects.filter(equipment_type=self.object)

        return context


class ViewEquipmentGuidePage(LoginRequiredMixin, DetailView):

    model = EquipmentGuide
    template_name = "webpage/student/view_guide.html"
    context_object_name = "equipment_guide"


class ViewAllGuidePage(ListView):

    model = EquipmentGuide
    template_name = "webpage/student/view_all_guide.html"
    context_object_name = "guides"

    def get_queryset(self):
        return EquipmentGuide.objects.filter(equipment_type_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment_type"] = EquipmentType.objects.get(id=self.kwargs["pk"])

        return context
