from django.urls import path
from .views import ManageRolesView


urlpatterns = [
    path("manage-roles/", ManageRolesView.as_view(), name="manage_roles"),
]
