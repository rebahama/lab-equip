from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Repair


class ShowAllRepair(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    model = Repair
    template_name = "repairs/show-active-history-repairs.html"

    def test_func(self):
        return self.request.user.groups.filter(name="Caretaker").exists()

    def handle_no_permission(self):
        return TemplateView.as_view(template_name="webpage/no_permission.html")(
            self.request
        )
