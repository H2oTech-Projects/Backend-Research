from django.urls import path
from .views import SwaggerAPIView, GoodbyeAPIView
from .views import BookAPIView, BookListCreateAPIView
urlpatterns = [
    path('hello/', SwaggerAPIView.as_view(), name='hello-world'),
    path('bye/', GoodbyeAPIView.as_view(), name='bye-world'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookAPIView.as_view(), name='book-detail'),
    
]
