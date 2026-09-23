from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Equipment, Category


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
        "name",
        "category",
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
        return context

    def handle_no_permission(self):
            return TemplateView.as_view(template_name="webpage/no_permission.html")(
                self.request
            )
