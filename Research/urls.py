from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = router.urls



'''path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),'''