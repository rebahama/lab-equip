from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

class CreatePageCaretakerView(TemplateView):
    template_name = "webpage/caretaker/create_caretaker.html"
