from django.views.generic import TemplateView
from .models import Profile

class ShowProfilePage(TemplateView):
    model = Profile
    template_name = "account/profile_page.html"