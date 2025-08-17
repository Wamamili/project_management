from rest_framework import serializers
from .models import Project, TeamMember
from accounts.serializers import UserSerializer
from accounts.models import User

class TeamMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    class Meta:
        model = TeamMember
        fields = ['id', 'user', 'user_id', 'project']

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='owner', write_only=True, required=False
    )
    team = TeamMemberSerializer(source='team_members', many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'owner', 'owner_id', 'start_date', 'end_date', 'team']
