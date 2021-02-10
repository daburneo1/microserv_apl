from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

routers = DefaultRouter()
routers.register(r'usuario', UserViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]