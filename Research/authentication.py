from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")

        if not token:
            raise AuthenticationFailed("Authentication token required.")

        if token != "valid_token":
            raise AuthenticationFailed("Invalid authentication token.")

        return ("user", None)  # Simulating a successful authentication
