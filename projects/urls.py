from django.urls import path
from .views import CreateProjectStudent, ViewCreatedProject


urlpatterns = [
    path("project/create/<int:pk>", CreateProjectStudent.as_view(), name="create-project"),
    path("project/view/<int:pk>", ViewCreatedProject.as_view(), name="show-projects"),
]
