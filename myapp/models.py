from django.db import models

# Create your models here.

class Teacher:
    name,surname = models.TextField()


class Subject:
    subject = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name="teacher/subject")


class Class:
    num_class = models.CharField(max_length=10)


class Student:
    full_name = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name="student/class")