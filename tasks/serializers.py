from rest_framework import serializers
from .models import Task, Comment
from accounts.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField(write_only=True, required=False)
    assigned_to_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'project_id', 'assigned_to', 'assigned_to_id',
                  'status', 'priority', 'due_date', 'created_by']

    def create(self, validated_data):
        project = validated_data.pop('project', None)
        if not project and 'project_id' in self.initial_data:
            from projects.models import Project
            project = Project.objects.get(id=self.initial_data['project_id'])
        assigned_to = None
        if 'assigned_to_id' in self.initial_data and self.initial_data['assigned_to_id']:
            from accounts.models import User
            assigned_to = User.objects.get(id=self.initial_data['assigned_to_id'])
        task = Task.objects.create(
            project=project,
            assigned_to=assigned_to,
            created_by=self.context['request'].user,
            **validated_data
        )
        return task

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'task', 'author', 'body', 'timestamp']
