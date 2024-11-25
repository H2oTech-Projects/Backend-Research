from rest_framework.routers import SimpleRouter
from rest_framework.routers import DynamicRoute

class CustomRouter(SimpleRouter):
    def get_default_basename(self, viewset):
        # Append '_custom' to all basenames
        return super().get_default_basename(viewset) + "_custom"

from rest_framework.routers import DynamicRoute, SimpleRouter

class Custom_Router(SimpleRouter):#dynamic routes
    routes = [

        DynamicRoute(
            url=r'^{prefix}/{lookup}/publisher$',  #  /books/{book_id}/publisher
            name='{basename}-publisher',          # The name of this URL
            detail=True,                          # Detail route (single object, not a list)
            initkwargs={}                         # Additional arguments (empty here)
        ),
    ]
