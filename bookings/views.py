from django.views.generic import TemplateView


class BookingCreateView(TemplateView):
     template_name = "booking/booking_form.html"
