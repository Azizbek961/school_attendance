from django.contrib import admin
from .models import Profile, Class, Subject, Attendance, Settings


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'phone', 'student_class']
    list_filter = ['role']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'phone']

    fieldsets = (
        ('Foydalanuvchi ma\'lumotlari', {
            'fields': ('user', 'role', 'phone', 'birth_date')
        }),
        ('O\'quvchi uchun', {
            'fields': ('student_class',),
            'classes': ('collapse',),
        }),
        ('O\'qituvchi uchun', {
            'fields': ('subjects',),
            'classes': ('collapse',),
        }),
    )


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'room', 'schedule', 'created_at']
    list_filter = ['teacher']
    search_fields = ['name', 'teacher__username', 'room']

    fieldsets = (
        (None, {
            'fields': ('name', 'teacher', 'room', 'schedule')
        }),
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'lessons_per_week', 'schedule', 'created_at']
    list_filter = ['teacher']
    search_fields = ['name', 'teacher__username']
    filter_horizontal = ['classes']

    fieldsets = (
        (None, {
            'fields': ('name', 'teacher', 'lessons_per_week', 'schedule')
        }),
        ('Sinflar', {
            'fields': ('classes',),
        }),
    )


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'class_obj', 'date', 'status', 'teacher', 'created_at']
    list_filter = ['status', 'date', 'subject', 'class_obj']
    search_fields = ['student__username', 'student__first_name', 'student__last_name']
    date_hierarchy = 'date'

    fieldsets = (
        ('Davomat ma\'lumotlari', {
            'fields': ('student', 'teacher', 'subject', 'class_obj', 'date', 'status')
        }),
        ('Qo\'shimcha ma\'lumot', {
            'fields': ('notes',),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ['created_at', 'updated_at']


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'academic_year', 'attendance_threshold', 'language']

    fieldsets = (
        ('Maktab ma\'lumotlari', {
            'fields': ('school_name', 'school_address', 'school_phone', 'school_email', 'academic_year')
        }),
        ('Davomat sozlamalari', {
            'fields': ('attendance_threshold', 'auto_attendance', 'notification_pref')
        }),
        ('Til sozlamalari', {
            'fields': ('language',)
        }),
    )

    def has_add_permission(self, request):
        # Faqat bitta Settings obyekti bo'lishi kerak
        return not Settings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Settings obyektini o'chirib bo'lmaydi
        return False