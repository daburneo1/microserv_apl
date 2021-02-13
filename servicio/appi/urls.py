from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

routers = DefaultRouter()
routers.register(r'course', CourseViewSet)
routers.register(r'institution', InstitutionViewSet)
routers.register(r'state', StateViewSet)
routers.register(r'usuario', UserViewSet)
routers.register(r'userprofile', UserProfileViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('courses/<int:pk>/', CourseDetailViewSet.as_view()),
]