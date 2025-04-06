from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    max_students = models.PositiveIntegerField(default=30)
    enrolled_students = models.ManyToManyField(User, blank=True, related_name="courses")
    time = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.course_id} - {self.name}"

    def is_full(self):
        return self.enrolled_students.count() >= self.max_students

class EnrollmentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=[('enrolled', 'Enrolled'), ('dropped', 'Dropped')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name} - {self.action} on {self.timestamp}"