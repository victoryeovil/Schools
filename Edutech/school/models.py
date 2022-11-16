from django.db import models

from portal.models import Student


# Create your models here.
class School(models.Model):
    choices = ['private']
    name = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=256, unique=True)
    cell = models.ManyToManyField()
    type = models.Choices(choices)
    subjects = models.ManyToManyField()
    sports = models.ManyToManyField()


class Subject(models.Model):
    name = models.CharField(max_length=256)
    topic = models.CharField(max_length=256)


class Assignment(models.Model):
    subject = models.ForeignKey(Subject.name, on_delete=models.CASCADE)
    topic = models.ForeignKey(Subject.topic, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="student_mark", on_delete=models.CASCADE)
    mark = models.DecimalField(decimal_places=2)


class Test(models.Model):
    subject = models.ForeignKey(Subject.name, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="student_marks", on_delete=models.CASCADE)
    mark = models.DecimalField(decimal_places=2)
