from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task, Comment
from .serializers import TaskSerializer, CommentSerializer
from .permissions import IsAssigneeOrProjectOwner, IsProjectOwnerOrTaskCreator
from projects.models import Project, TeamMember

def is_member(user, project):
    if project.owner_id == user.id:
        return True
    return TeamMember.objects.filter(project=project, user=user).exists()

class ProjectTaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        if not is_member(self.request.user, project):
            return Task.objects.none()
        return Task.objects.filter(project=project).select_related('project', 'assigned_to', 'created_by')

    def create(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        if not is_member(request.user, project):
            return Response({'detail': 'Not a project member.'}, status=status.HTTP_403_FORBIDDEN)
        data = request.data.copy()
        data['project_id'] = project.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.select_related('project', 'assigned_to', 'created_by')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAssigneeOrProjectOwner, IsProjectOwnerOrTaskCreator]

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        data = request.data.copy()
        data['task'] = task.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, task=task)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
