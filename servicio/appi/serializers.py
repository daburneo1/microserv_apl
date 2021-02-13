from rest_framework import serializers, generics
from django.contrib.auth.models import User
from .models import (Course,Institution,State,UserProfile)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'





class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
