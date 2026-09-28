from django.urls import path
from .views import (
    BookingCreateView,

)

urlpatterns = [
    path("booking", BookingCreateView.as_view(), name="create-booking"),

]
