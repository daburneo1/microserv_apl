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
        fields = ['user','rol_student','rol_teacher']


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['course','student','state','info']

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ['nameInstitution']

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['nameCourse','numHours','edition','price','date','institution','instructor','student']


class CourseSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()
    instructor = UserSerializer()
    student = UserSerializer(many=True)
    class Meta:
        model = Course
        fields = ['nameCourse','numHours','edition','price','date','institution','instructor','student']

