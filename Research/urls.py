from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet , BookViewSet, PublisherViewSet
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .routers import CustomRouter #Custom_Router
from .views import ProductListCreateView, product_detail,order_detail, OrderListCreateView
from .routers import api_view_router

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')

nested_router = NestedSimpleRouter(router, r'authors', lookup='author')
nested_router.register(r'books', BookViewSet, basename='author-books')

custom_routers = CustomRouter()
custom_routers.register(r'publishers', PublisherViewSet, basename='publisher')

'''customized_routers = Custom_Router()
customized_routers.register(r'books', BookViewSet, basename= 'book')'''


urlpatterns = [
    *router.urls,
    *nested_router.urls,
    *custom_routers.urls,
    *api_view_router(view=ProductListCreateView, basename='products', nested=True),
    *api_view_router(view=ProductListCreateView, basename='products', nested=False),
    
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

'''
*api_view_router(view=product_detail, basename='products', nested=True),
    *api_view_router(view=product_detail, basename='products', nested=False),
path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),'''