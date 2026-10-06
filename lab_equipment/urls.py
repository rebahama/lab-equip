from django.contrib import admin
from .views import (
    HomePageView,
)
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", HomePageView.as_view(), name="home"),
    path("", include("accounts.urls")),
    path("", include("equipment.urls")),
    path("", include("bookings.urls")),
    path("", include("profiles.urls")),
    path("", include("repairs.urls")),
]
