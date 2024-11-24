from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet , BookViewSet
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')

nested_router = NestedSimpleRouter(router, r'authors', lookup='author')
nested_router.register(r'books', BookViewSet, basename='author-books')

urlpatterns = [
    *router.urls,
    *nested_router.urls,
]

'''path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),'''