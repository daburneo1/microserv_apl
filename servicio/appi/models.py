from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    nameCourse = models.CharField(max_length=40)
    numHours = models.IntegerField()
    edition = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
    institution = models.ForeignKey('Institution',default=True, on_delete=models.PROTECT, related_name='course_institution')
    instructor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='course_instructor')
    student = models.ManyToManyField(User, db_index=True, through="State")

    def __str__(self):
        return self.nameCourse


class Institution(models.Model):
    nameInstitution = models.CharField(max_length=30)

    def __str__(self):
        return self.nameInstitution


class State(models.Model):
    course = models.ForeignKey('Course', on_delete=models.PROTECT, related_name='state_course')
    student = models.ForeignKey(User, on_delete=models.PROTECT)
    state = models.ForeignKey('CourseState', on_delete=models.PROTECT, related_name='state', blank=True, null=True)
    info = models.CharField(max_length=40,blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name='userprofile'
    )
    rol_student = models.BooleanField(default=False)
    rol_teacher = models.BooleanField(default=False)

class CourseState(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.estado