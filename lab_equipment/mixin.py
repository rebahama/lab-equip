from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView


class CaretakerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Created to check if the user is logged in and have a Caretaker group role, if not
    display the no permission page.
    """

    def test_func(self):
        return self.request.user.groups.filter(
            name="Caretaker"
        ).exists()

    def handle_no_permission(self):
        return TemplateView.as_view(
            template_name="webpage/no_permission.html"
        )(self.request)


class StudentRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Created to check if the user is logged in and a Student group role, if not
    display the no permission page.
    """

    def test_func(self):
        return self.request.user.groups.filter(
            name="Student"
        ).exists()

    def handle_no_permission(self):
        return TemplateView.as_view(
            template_name="webpage/no_permission.html"
        )(self.request)
