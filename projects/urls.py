from django.urls import path
from .views import CreateProjectStudent


urlpatterns = [
    path("project/create/<int:pk>", CreateProjectStudent.as_view(), name="create-project"),
]
