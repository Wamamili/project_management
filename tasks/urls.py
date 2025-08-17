from django.urls import path
from .views import ProjectTaskListCreateView, TaskRetrieveUpdateDestroyView, CommentCreateView

urlpatterns = [
    path('projects/<int:project_id>/tasks/', ProjectTaskListCreateView.as_view(), name='project-task-list-create'),
    path('<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='task-comment'),
]
