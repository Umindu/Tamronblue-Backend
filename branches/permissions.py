from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    # Custom permission to only allow agents to access the endpoint.
    def has_permission(self, request, view):
        # Check if the user has the role of "agent"
        return request.user and request.user.is_authenticated and request.user.is_admin
