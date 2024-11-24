from rest_framework.routers import SimpleRouter

class CustomRouter(SimpleRouter):
    def get_default_basename(self, viewset):
        # Append '_custom' to all basenames
        return super().get_default_basename(viewset) + "_custom"
