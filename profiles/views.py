from django.views.generic import UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Profile


class ShowProfilePage(
    UpdateView,
    LoginRequiredMixin
):
    """
        Only the logged in user can edit profile, if there is no profile
        then one will be created when visiting the page frst time.
    """

    model = Profile
    template_name = "account/profile_page.html"
    fields = [
        "first_name",
        "last_name",
    ]

    context_object_name = "profile"

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        messages.success(
            self.request, "Profile updated successfully.", extra_tags="profile"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("profile-page")
