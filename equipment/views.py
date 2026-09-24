from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Equipment, Category, EquipmentType, Location


class CreatePageCaretakerView(
    LoginRequiredMixin,
    UserPassesTestMixin,
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
        "description",
        "serial_number",
        "location",
        "status",
        "condition",
        "image",
    ]
    success_url = "/"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()
        context["equipment_types"] = EquipmentType.objects.all()
        context["locations"] = Location.objects.all()

        return context

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )


class ViewAllStudent(LoginRequiredMixin, TemplateView):
    """Display all equipment to users"""

    model = Equipment
    template_name = "webpage/student/view_all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        equipment = Equipment.objects.all().order_by("-created_at")

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

        context["on_loan_count"] = equipment_queryset.filter(
            status="on_loan"
        ).count()

        context["total_count"] = equipment_queryset.count()

        return context

class ViewCategoryPage(TemplateView):
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

        context["categories"] = categories

        return context

class ViewCategoryDetailPage(DetailView):
    """Display the only the specfik categories that was clicked on """

    model = Category
    template_name = "webpage/caretaker/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["equipment"] = Equipment.objects.filter(
            equipment_type__category=self.object
        )

        return context
