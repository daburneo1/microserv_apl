from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import (UserSerializer,InstitutionSerializer, StateSerializer, CourseSerializer,UserProfileSerializer,CourseDetailSerializer,CourseStateSerializer)
from .models import (UserProfile, Course, Institution,State,CourseState)


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailViewSet(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CourseStateViewSet(viewsets.ModelViewSet):
    queryset = CourseState.objects.all()
    serializer_class = CourseStateSerializer