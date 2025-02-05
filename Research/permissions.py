from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            raise PermissionDenied("You do not have admin privileges.")
        return True
