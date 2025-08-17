from django.db import models
from django.conf import settings

# Custom User
User = settings.AUTH_USER_MODEL

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_memberships')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='team_members')

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user} -> {self.project}"
