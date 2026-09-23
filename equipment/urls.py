from django.urls import path
from .views import (CreatePageCaretakerView
)

urlpatterns = [
    path("create", CreatePageCaretakerView.as_view(), name="create"),
]
