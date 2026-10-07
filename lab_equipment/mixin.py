from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView


class CaretakerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(
            name="Caretaker"
        ).exists()

    def handle_no_permission(self):
        return TemplateView.as_view(
            template_name="webpage/no_permission.html"
        )(self.request)


class StudentRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(
            name="Student"
        ).exists()

    def handle_no_permission(self):
        return TemplateView.as_view(
            template_name="webpage/no_permission.html"
        )(self.request)
