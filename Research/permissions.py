'''from rest_framework.permissions import BasePermission
class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Check if the book's author is the one making the request
        return obj.author.user == request.user'''