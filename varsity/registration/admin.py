from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Course
from .models import EnrollmentHistory

# Show the number of enrolled students in the Course admin list view
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'name', 'instructor', 'max_students', 'enrolled_count')
    filter_horizontal = ('enrolled_students',)  # Allows easy enrollment management

    def enrolled_count(self, obj):
        return obj.enrolled_students.count()
    enrolled_count.short_description = 'Enrolled Students'

# Inline admin to show which courses a student is enrolled in
class EnrolledCoursesInline(admin.TabularInline):
    model = Course.enrolled_students.through  # The intermediate table for ManyToMany relationship
    extra = 0
    verbose_name = "Enrolled Course"
    verbose_name_plural = "Enrolled Courses"
    can_delete = False

# Unregister the default User admin and re-register with inline
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    inlines = (EnrolledCoursesInline,)  # Show enrolled courses in user admin

@admin.register(EnrollmentHistory)
class EnrollmentHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'action', 'timestamp')
    list_filter = ('action', 'timestamp')
    search_fields = ('user__username', 'course__name')