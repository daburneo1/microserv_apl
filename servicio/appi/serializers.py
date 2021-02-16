from rest_framework import serializers, generics
from django.contrib.auth.models import User
from .models import (Course,Institution,State,UserProfile,CourseState)

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
        fields = ['id','course','student','state','info','link']

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ['id','nameInstitution']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','nameCourse','numHours','edition','price','date','institution','instructor','student']

class CourseStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseState
        fields = ['id','estado']

class CourseDetailSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()
    instructor = UserSerializer()
    student = UserSerializer(many=True,read_only=True) # Se implemeta cuando es Foreign Key
    state = serializers.SerializerMethodField()
    def get_state(self,obj):
        state = obj.state_course.all()
        serializers = StateSerializer(instance=state,many=True)
        return serializers.data

    class Meta:
        model = Course
        fields = ['id','nameCourse','numHours','edition','price','date','institution','instructor','student','state']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','nameCourse','numHours','edition','price','date','institution','instructor','student']