from django.urls import path
from .views import ProjectTaskListCreateView, TaskRetrieveUpdateDestroyView, CommentCreateView

urlpatterns = [
    path("", ProjectTaskListCreateView.as_view(), name="project-task-list-create"),  # /api/projects/<id>/tasks/
    path("<int:pk>/", TaskRetrieveUpdateDestroyView.as_view(), name="task-detail"),  # /api/projects/<id>/tasks/<id>/
    path("<int:pk>/comment/", CommentCreateView.as_view(), name="task-comment"),     # /api/projects/<id>/tasks/<id>/comment/
]
