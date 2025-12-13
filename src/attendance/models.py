# attendance/models.py
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', "O'quvchi"),
        ('teacher', "O'qituvchi"),
        ('admin', 'Administrator'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    # For students
    student_class = models.ForeignKey('Class', on_delete=models.SET_NULL,
                                      null=True, blank=True, related_name='students')

    # For teachers
    subjects = models.ManyToManyField('Subject', blank=True, related_name='teachers')

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

    def get_role_display(self):
        role_display = {
            'student': "O'quvchi",
            'teacher': "O'qituvchi",
            'admin': 'Admin',
        }
        return role_display.get(self.role, self.role)


class Class(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='teacher_classes')
    room = models.CharField(max_length=20, blank=True, null=True)
    schedule = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='teacher_subjects')
    classes = models.ManyToManyField(Class, related_name='subjects')
    lessons_per_week = models.IntegerField(default=1)
    schedule = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taken_attendances')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='present')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.student.username} - {self.subject.name} - {self.date}"


class Settings(models.Model):
    school_name = models.CharField(max_length=200, default='SAMO International School')
    school_address = models.TextField(blank=True, null=True)
    school_phone = models.CharField(max_length=20, blank=True, null=True)
    school_email = models.EmailField(blank=True, null=True)
    academic_year = models.CharField(max_length=20, default='2023-2024')
    attendance_threshold = models.IntegerField(default=85)
    auto_attendance = models.BooleanField(default=False)
    notification_pref = models.BooleanField(default=True)
    language = models.CharField(max_length=10, default='uz')

    def __str__(self):
        return "Tizim sozlamalari"