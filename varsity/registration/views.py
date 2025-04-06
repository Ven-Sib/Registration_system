from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CourseEnrollForm
from .models import Course
from .models import EnrollmentHistory

def home(request):
    return render(request, 'registration/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    all_courses = Course.objects.all()
    user_courses = request.user.courses.all()
    return render(request, 'registration/dashboard.html', {
        'user_courses': user_courses,
        'all_courses': all_courses
    })

@login_required
def enroll_course(request):
    if request.method == 'POST':
        form = CourseEnrollForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            
            # Check if already enrolled
            if course.enrolled_students.filter(id=request.user.id).exists():
                return render(request, 'registration/enroll.html', {
                    'form': form,
                    'error': 'You are already enrolled in this course.'
                })

            # Check if course is full
            if course.is_full():
                return render(request, 'registration/enroll.html', {
                    'form': form,
                    'error': 'Course is full!'
                })

            # Enroll the user in the course
            course.enrolled_students.add(request.user)
            
            # Log the enrollment in history
            EnrollmentHistory.objects.create(
                user=request.user,
                course=course,
                action='enrolled'
            )
            
            return redirect('dashboard')
    else:
        form = CourseEnrollForm()
    return render(request, 'registration/enroll.html', {'form': form})

@login_required
def drop_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.enrolled_students.remove(request.user)
    
    # Log the dropout in history
    EnrollmentHistory.objects.create(
        user=request.user,
        course=course,
        action='dropped'
    )
    
    return redirect('dashboard')
