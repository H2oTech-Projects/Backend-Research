from django.urls import path
from .views import ProductDetailView, ThirdPartyServiceView, UserView, ExampleView, SecureView, AdminOnlyView

urlpatterns = [
  path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
  path('thirdparty/', ThirdPartyServiceView.as_view(), name='third-party'),
  path('user/', UserView.as_view(), name='user'),
  path('example/', ExampleView.as_view(), name='example'),
  path('secure/', SecureView.as_view(), name='secure'),
  path('adminonly/', AdminOnlyView.as_view(), name='adminonly'),
]
