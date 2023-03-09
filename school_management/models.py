from django.db import models
from django.contrib.auth.models import User


class SchoolClass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    classes = models.ManyToManyField(SchoolClass, related_name='subjects')

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='students')

    def __str__(self):
        return self.user.get_full_name()


class Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.student} {self.subject} {self.marks}'

    def get_grade(self):
        if self.marks >= 80:
            return 'A+'
        elif self.marks >= 70:
            return 'A'
        elif self.marks >= 60:
            return 'A-'
        elif self.marks >= 50:
            return 'B'
        elif self.marks >= 40:
            return 'C'
        elif self.marks >= 33:
            return 'D'
        else:
            return 'F'
