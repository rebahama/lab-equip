from django.views.generic import TemplateView


class CareTakerDashboard(TemplateView):
    template_name = "webpage/caretaker/caretaker_dashboard.html"