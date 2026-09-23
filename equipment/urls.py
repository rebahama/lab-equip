from django.urls import path
from .views import (
    CreatePageCaretakerView,
    ViewAllStudent,
)

urlpatterns = [
    path("create", CreatePageCaretakerView.as_view(), name="create"),
    path("showall", ViewAllStudent.as_view(), name="show-student"),
]
