from django.contrib import admin
from django.urls import path
from Research.views import StudentApi,LoginApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',StudentApi.as_view()),
    path('login/',LoginApi.as_view()),

]