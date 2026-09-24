from django.urls import path
from .views import (
    CreatePageCaretakerView,
    ViewAllStudent,
    ViewAllDetailPage,
    ViewCategoryPage,
    ViewCategoryDetailPage,
)

urlpatterns = [
    path("create", CreatePageCaretakerView.as_view(), name="create"),
    path("showall", ViewAllStudent.as_view(), name="show-student"),
    path("detail/<int:pk>", ViewAllDetailPage.as_view(), name="show-detail"),
    path("category", ViewCategoryPage.as_view(), name="show-category"),
    path("category/<int:pk>/",ViewCategoryDetailPage.as_view(), name="category-detail",),
]
