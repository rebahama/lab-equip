from django.urls import path
from .views import CreateProjectStudent, ViewCreatedProject, ViewDetaliedProjects


urlpatterns = [
    path("project/create/<int:pk>", CreateProjectStudent.as_view(), name="create-project"),
    path("project/view/<int:pk>", ViewCreatedProject.as_view(), name="show-projects"),
    path("project/view/detail/<int:pk>", ViewDetaliedProjects.as_view(), name="detail-projects"),
]
