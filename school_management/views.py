from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SchoolClass, Subject, Student, Exam

@login_required
def add_class(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        SchoolClass.objects.create(name=name)
        messages.success(request, 'Class added successfully.')
        return redirect('dashboard')
    return render(request, 'add_class.html')

@login_required
def add_subject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        classes = request.POST.getlist('classes')
        subject = Subject.objects.create(name=name)
        for cls_id in classes:
            subject.classes.add(cls_id)
        messages.success(request, 'Subject added successfully.')
        return redirect('dashboard')
    classes = SchoolClass.objects.all()
    return render(request, 'add_subject.html', {'classes': classes})

@login_required
def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        school_class_id = request.POST.get('school_class')
        subjects = request.POST.getlist('subjects')
        user = User.objects.create_user(username=username, password=password,
                                        first_name=first_name, last_name=last_name)
        student = Student.objects.create(user=user, school_class_id=school_class_id)
        for subject_id in subjects:
            student.subjects.add(subject_id)
        messages.success(request, 'Student added successfully.')
        return redirect('dashboard')
    classes = SchoolClass.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'add_student.html', {'classes': classes, 'subjects': subjects})

@login_required
def add_exam(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        marks = request.POST.get('marks')
        Exam.objects.create(student_id=student_id, subject_id=subject_id, marks=marks)
        messages.success(request, 'Exam added successfully.')
        return redirect('dashboard')
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'add_exam.html', {'students': students, 'subjects': subjects})

def dashboard(request):
    if request.method == 'POST':
        class_id = request.POST.get('class')
        subject_id = request.POST.get('subject')
        if subject_id:
            exams = Exam.objects.filter(student__school_class_id=class_id,
                                        subject_id=subject_id).order_by('-marks')
        else:
            exams = Exam.objects.filter(student__school_class_id=class_id).order_by('subject__name', '-marks')
        return render(request, 'dashboard.html', {'exams': exams})
    classes = SchoolClass.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'dashboard.html', {'classes': classes, 'subjects': subjects})
