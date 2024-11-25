from rest_framework.routers import SimpleRouter
from rest_framework.routers import DynamicRoute
from .views import product_detail , ProductListCreateView, order_detail, OrderListCreateView

from django.urls import path


class CustomRouter(SimpleRouter):
    def get_default_basename(self, viewset):
        # Append '_custom' to all basenames
        return super().get_default_basename(viewset) + "_custom"

from rest_framework.routers import DynamicRoute, SimpleRouter
'''
class Custom_Router(SimpleRouter):#dynamic routes
    routes = [

        DynamicRoute(
            url=r'^{prefix}/{lookup}/publisher$',  #  /books/{book_id}/publisher
            name='{basename}-publisher',          # The name of this URL
            detail=True,                          # Detail route (single object, not a list)
            initkwargs={}                         # Additional arguments (empty here)
        ),
    ]
'''
'''
def api_view_router(view, basename):
    return [
        path(f'{basename}/', ProductListCreateView.as_view(), name=f'{basename}-list-create'),
        path(f'{basename}/<int:pk>/', product_detail.as_view(), name=f'{basename}-detail'),
    ]'''

def api_view_router(view, basename, nested=False):
    if nested:
        return [
            path(f'{basename}/', ProductListCreateView.as_view(), name=f'{basename}-list-create'),
            path(f'{basename}/<int:pk>/', product_detail.as_view(), name=f'{basename}-detail'),      
        ]
    else:
        return [
            path(f'{basename}/<int:pk>/orders/', OrderListCreateView.as_view(), name=f'{basename}-list-create'),
            path(f'{basename}/<int:pk>/orders/<int:order_pk>/', order_detail.as_view(), name=f'{basename}-detail'),
        ]