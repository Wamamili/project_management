from rest_framework.permissions import BasePermission

class IsAssigneeOrProjectOwner(BasePermission):
    message = 'Only the task assignee or project owner may modify this task.'

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        is_assignee = obj.assigned_to_id == request.user.id if obj.assigned_to_id else False
        is_owner = getattr(obj.project, 'owner_id', None) == request.user.id
        return is_assignee or is_owner

class IsProjectOwnerOrTaskCreator(BasePermission):
    message = 'Only the project owner or task creator may delete this task.'

    def has_object_permission(self, request, view, obj):
        if request.method != 'DELETE':
            return True
        is_owner = getattr(obj.project, 'owner_id', None) == request.user.id
        is_creator = obj.created_by_id == request.user.id
        return is_owner or is_creator
