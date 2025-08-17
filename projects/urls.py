from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView, AddMemberView

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('<int:pk>/add_member/', AddMemberView.as_view(), name='project-add-member'),
]
