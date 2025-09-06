from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Project, TeamMember
from .serializers import ProjectSerializer, TeamMemberSerializer
from .permissions import IsProjectOwner
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from tasks.models import Task


class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(
            Q(owner=user) | Q(team_members__user=user)
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all().select_related('owner')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        project = self.get_object()
        self.check_object_permissions(request, project)
        if project.owner != request.user:
            return Response({'detail': 'Only the owner can update this project.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        if project.owner != request.user:
            return Response({'detail': 'Only the owner can delete this project.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

class AddMemberView(generics.CreateAPIView):
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        project_id = kwargs.get('pk')
        project = Project.objects.get(pk=project_id)
        if project.owner != request.user:
            return Response({'detail': 'Only the owner can add members.'}, status=status.HTTP_403_FORBIDDEN)
        data = request.data.copy()
        data['project'] = project_id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

def is_member(user, project):
    if user.is_superuser or project.owner == user:
        return True
    return TeamMember.objects.filter(project=project, user=user).exists()

@login_required
def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if not is_member(request.user, project):
        return HttpResponseForbidden("You are not authorized to view this project.")

    tasks = Task.objects.filter(project=project).select_related("assigned_to", "created_by")
    members = TeamMember.objects.filter(project=project).select_related("user")

    return render(request, "projects/project_detail.html", {
        "project": project,
        "tasks": tasks,
        "members": members,
    })

