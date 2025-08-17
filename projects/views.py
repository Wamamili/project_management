from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Project, TeamMember
from .serializers import ProjectSerializer, TeamMemberSerializer
from .permissions import IsProjectOwner

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
