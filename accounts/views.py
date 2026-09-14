from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect


class ManageRolesView(UserPassesTestMixin, TemplateView):
    template_name = "account/manage_roles.html"

    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, *args, **kwargs):
        user_id = request.POST.get("user_id")
        group_name = request.POST.get("group")

        user = User.objects.get(id=user_id)
        group = Group.objects.get(name=group_name)

        user.groups.clear()
        user.groups.add(group)

        messages.success(request, f"{user.username}'s role was changed successfully.")

        return redirect("manage_roles")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["users"] = User.objects.all()
        context["groups"] = Group.objects.filter(name__in=["Student", "Caretaker"])

        return context
