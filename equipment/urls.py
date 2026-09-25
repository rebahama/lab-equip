from django.urls import path
from .views import (
    CreatePageCaretakerView,
    ViewAllStudent,
    ViewAllDetailPage,
    ViewCategoryPage,
    ViewCategoryDetailPage,
)
from .views_caretaker import(
    CareTakerDashboard,
    EditEquipmentView,
    DeleteEquipmentView
)

urlpatterns = [
    path("create", CreatePageCaretakerView.as_view(), name="create"),
    path("showall", ViewAllStudent.as_view(), name="show-student"),
    path("detail/<int:pk>", ViewAllDetailPage.as_view(), name="show-detail"),
    path("category", ViewCategoryPage.as_view(), name="show-category"),
    path("category/<int:pk>/",ViewCategoryDetailPage.as_view(), name="category-detail",),
    path("caretakerdash", CareTakerDashboard.as_view(), name="show-dashboard"),
    path("detail/<int:pk>/edit/", EditEquipmentView.as_view(), name="equipment-edit"),
    path("delete/<int:pk>/delete/", DeleteEquipmentView.as_view(), name="equipment-delete"),
]
