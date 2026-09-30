from django.urls import path
from .views import ShowProfilePage


urlpatterns = [
    path("profile", ShowProfilePage.as_view(), name="create-booking"),
]
