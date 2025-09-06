from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView, AddMemberView, project_detail_view

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('<int:pk>/add_member/', AddMemberView.as_view(), name='project-add-member'),
    path("<int:pk>/", project_detail_view, name="project_detail"),
]
