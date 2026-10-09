from django.views.generic import UpdateView, TemplateView
from django.contrib import messages
from lab_equipment.mixin import StudentRequiredMixin


class CreateProjectStudent(StudentRequiredMixin, TemplateView):
    
    template_name = "projects/create_project.html"
