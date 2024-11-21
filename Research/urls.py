from django.urls import path
from . import views

urlpatterns = [
    path('my_view/', views.my_view, name='my_view'),
    
]
'''path('info/', views.info_view, name='info_view'),
    path('debug/', views.debug_view, name='debug_view'),
    path('warning/', views.warning_view, name='warning_view'),
    path('error/', views.error_view, name='error_view'),
    path('my_view/', views.my_view, name='my_view'),
    path('error_view/', views.error_view, name='error_view'),'''