from django.contrib import admin
from .models import SchoolClass
from .models import Subject
from .models import Student
from .models import Exam
# Register your models here.

admin.site.register(SchoolClass)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Exam)
