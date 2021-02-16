from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

routers = DefaultRouter() # Crea automaticamente los enlaces segun el nombre y vista proporcionado
routers.register(r'course', CourseViewSet)
routers.register(r'institution', InstitutionViewSet)
routers.register(r'state', StateViewSet)
routers.register(r'usuario', UserViewSet)
routers.register(r'userprofile', UserProfileViewSet)
routers.register(r'coursestate', CourseStateViewSet)

urlpatterns = [
    path('', include(routers.urls)), # Todos los enlaces generados son registrados en el framework
    path('courses/<int:pk>/', CourseDetailViewSet.as_view()), # Detalle de curso
]