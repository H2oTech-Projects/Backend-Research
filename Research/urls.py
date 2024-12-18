from django.urls import path
from .views import SwaggerAPIView, GoodbyeAPIView

urlpatterns = [
    path('hello/', SwaggerAPIView.as_view(), name='hello-world'),
    path('bye/', GoodbyeAPIView.as_view(), name='bye-world'),
]
