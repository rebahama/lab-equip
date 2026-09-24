from django.urls import path
from .views import (
    CreatePageCaretakerView,
    ViewAllStudent,
    ViewAllDetailPage,
)

urlpatterns = [
    path("create", CreatePageCaretakerView.as_view(), name="create"),
    path("showall", ViewAllStudent.as_view(), name="show-student"),
    path("detail/<int:pk>", ViewAllDetailPage.as_view(), name="show-detail"),
]
