from django.urls import path, include
from . import views

urlpatterns = [
    path('add-class/', views.add_class, name='add_class'),
    path('add-subject/', views.add_subject, name='add_subject'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-exam/', views.add_exam, name='add_exam'),
    path('', views.dashboard, name='dashboard'),
]
