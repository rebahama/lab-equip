from django.urls import path
from .views import (
    CreatePageCaretakerView,
    ViewAllStudent,
    ViewAllDetailPage,
    ViewCategoryPage,
    ViewCategoryDetailPage,
    ViewEquipmentTypeDetailPage
)
from .views_caretaker import(
    CareTakerDashboard,
    EditEquipmentView,
    DeleteEquipmentView,
    EditCategoryPage,
    EditEquipmentType,
    ViewNotInServiceEquipment,
    CreateEquipmentGuide
)

urlpatterns = [
    path("create", CreatePageCaretakerView.as_view(), name="create"),
    path("showall", ViewAllStudent.as_view(), name="show-student"),
    path("detail/<int:pk>", ViewAllDetailPage.as_view(), name="show-detail"),
    path("category", ViewCategoryPage.as_view(), name="show-category"),
    path("category/<int:pk>/",ViewCategoryDetailPage.as_view(), name="category-detail"),
    path("caretakerdash", CareTakerDashboard.as_view(), name="show-dashboard"),
    path("detail/<int:pk>/edit/", EditEquipmentView.as_view(), name="equipment-edit"),
    path("delete/<int:pk>/delete/", DeleteEquipmentView.as_view(), name="equipment-delete"),
    path("category/<int:pk>/edit", EditCategoryPage.as_view(), name="category-detail-edit"),
    path("equipment-type/<int:pk>/", ViewEquipmentTypeDetailPage.as_view(), name="equipment-type-detail"),
    path("category/equipment-type/<int:pk>/", EditEquipmentType.as_view(), name="edit-equipment-type"),
    path("showall/notservice", ViewNotInServiceEquipment.as_view(), name="show-not-service"),
    path("equipment-guide/<int:pk>/create", CreateEquipmentGuide.as_view(), name="create-guide"),
]
