# attendance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Qolgan URL'lar...

    path('users/', views.manage_users, name='manage_users'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),

    # ========== CLASS MANAGEMENT ==========
    path('classes/', views.manage_classes, name='manage_classes'),
    path('classes/add/', views.add_class, name='add_class'),
    path('classes/edit/<int:class_id>/', views.edit_class, name='edit_class'),
    path('classes/delete/<int:class_id>/', views.delete_class, name='delete_class'),

    # ========== SUBJECT MANAGEMENT ==========
    path('subjects/', views.manage_subjects, name='manage_subjects'),
    path('subjects/add/', views.add_subject, name='add_subject'),
    path('subjects/edit/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    path('subjects/delete/<int:subject_id>/', views.delete_subject, name='delete_subject'),

    # ========== ATTENDANCE MANAGEMENT ==========
    path('attendance/', views.manage_attendance, name='manage_attendance'),
    path('attendance/take/', views.take_attendance, name='take_attendance'),
    path('attendance/edit/<int:attendance_id>/', views.edit_attendance, name='edit_attendance'),
    path('attendance/delete/<int:attendance_id>/', views.delete_attendance, name='delete_attendance'),
    path('attendance/get-class-students/<int:class_id>/', views.get_class_students, name='get_class_students'),
    path('attendance/<int:attendance_id>/details/', views.attendance_details, name='attendance_details'),  # New


    # ========== STATISTICS ==========
    path('statistics/', views.statistics, name='statistics'),

    # ========== REPORTS ==========
    path('reports/', views.reports, name='reports'),
    path('reports/generate/', views.generate_report, name='generate_report'),
    path('reports/preview/', views.preview_report, name='preview_report'),

    # ========== SETTINGS ==========
    path('settings/', views.settings_view, name='settings'),

    # ========== AJAX ENDPOINTS ==========
    path('api/class/<int:class_id>/students/', views.get_class_students, name='get_class_students'),
    path('api/subject/<int:subject_id>/info/', views.get_subject_info, name='get_subject_info'),

    # ========== STUDENT DASHBOARD ==========
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),

    # ========== TEACHER DASHBOARD ==========
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    path('statistics/', views.statistics, name='statistics'),
    path('statistics/class-stats/', views.class_stats_json, name='class_stats_json'),
    path('statistics/trend-data/', views.trend_data_json, name='trend_data_json'),
    path('statistics/top-students/', views.top_students_json, name='top_students_json'),
    path('statistics/low-attendance/', views.low_attendance_json, name='low_attendance_json'),
    path('statistics/subjects/', views.subjects_json, name='subjects_json'),

    path('teacher/my-subjects/', views.teacher_my_subjects, name='teacher_my_subjects'),
    path('teacher/subject/<int:subject_id>/details/', views.teacher_subject_details_json,
         name='teacher_subject_details_json'),
    path('teacher/subject/<int:subject_id>/classes/', views.teacher_subject_classes_json,
         name='teacher_subject_classes_json'),

    path('teacher/my-classes/', views.teacher_my_classes, name='teacher_my_classes'),
    path('teacher/class/<int:class_id>/students/', views.teacher_class_students_json,
         name='teacher_class_students_json'),
    path('teacher/class/<int:class_id>/details/', views.teacher_class_details_json, name='teacher_class_details_json'),
    path('teacher/class/<int:class_id>/take-attendance/', views.teacher_take_class_attendance,
         name='teacher_take_class_attendance'),
    path('teacher/class/<int:class_id>/take-attendance/<int:subject_id>/', views.teacher_take_class_attendance,
         name='teacher_take_class_attendance_with_subject'),
    path('teacher/class/<int:class_id>/attendance/', views.teacher_view_class_attendance,
         name='teacher_view_class_attendance'),

    path('teacher/my-attendance/', views.teacher_my_attendance, name='teacher_my_attendance'),
    path('teacher/today-attendance/', views.teacher_today_attendance, name='teacher_today_attendance'),
    path('teacher/edit-attendance/<int:attendance_id>/', views.teacher_edit_attendance, name='teacher_edit_attendance'),
    path('teacher/delete-attendance/<int:attendance_id>/', views.teacher_delete_attendance,
         name='teacher_delete_attendance'),
    path('teacher/attendance-details/<int:attendance_id>/', views.teacher_attendance_details_json,
         name='teacher_attendance_details_json'),
    path('teacher/export-attendance/', views.teacher_export_attendance, name='teacher_export_attendance'),
    path('teacher/bulk-delete-attendance/', views.teacher_bulk_delete_attendance,
         name='teacher_bulk_delete_attendance'),
    path('teacher/take-attendance-form/', views.teacher_take_attendance_form, name='teacher_take_attendance_form'),
    path('teacher/class/<int:class_id>/subjects/', views.teacher_class_subjects_json,
         name='teacher_class_subjects_json'),
    path('teacher/today-schedule/', views.teacher_today_schedule_json, name='teacher_today_schedule_json'),

    path('teacher/reports/', views.teacher_reports, name='teacher_reports'),
    path('teacher/generate-report/', views.teacher_generate_report, name='teacher_generate_report'),
    path('teacher/export-report/', views.teacher_export_report, name='teacher_export_report'),
    path('teacher/report-chart-data/', views.teacher_report_chart_data, name='teacher_report_chart_data'),
    path('teacher/class/<int:class_id>/take-attendance/', views.teacher_take_class_attendance, name='teacher_take_class_attendance'),
    path('teacher/class/<int:class_id>/take-attendance/<int:subject_id>/', views.teacher_take_class_attendance, name='teacher_take_class_attendance_with_subject'),

    path('teacher/take-attendance-form/', views.teacher_take_attendance_form, name='teacher_take_attendance_form'),
    path('teacher/subject/<int:subject_id>/classes/', views.teacher_subject_classes_json,
         name='teacher_subject_classes_json'),
    path('teacher/today-schedule/', views.teacher_today_schedule_json, name='teacher_today_schedule_json'),
    path('teacher/class/<int:class_id>/take-attendance/<int:subject_id>/', views.teacher_take_class_attendance,
         name='teacher_take_class_attendance'),
    path('teacher/edit/attendance/', views.teacher_edit_attendance, name='teacher_edit_attendance'),

    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/dashboard-data/', views.student_dashboard_data, name='student_dashboard_data'),
    path('student/subject-performance/', views.student_subject_performance, name='student_subject_performance'),
    path('student/class-rankings/', views.student_class_rankings, name='student_class_rankings'),
    path('student/attendance-history/', views.student_attendance_history, name='student_attendance_history'),
    path('student/statistics/', views.student_statistics, name='student_statistics'),
    path('student/my-classes/', views.student_my_classes, name='student_my_classes'),
    path('student/notifications/', views.student_notifications, name='student_notifications'),
    path('student/settings/', views.student_settings, name='student_settings'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/schedule/', views.student_schedule, name='student_schedule'),
    path('student/tasks/', views.student_tasks, name='student_tasks'),
    path('student/messages/', views.student_messages, name='student_messages'),
    path('student/events/', views.student_events, name='student_events'),
    path('student/reports/', views.student_reports, name='student_reports'),

    # AJAX endpoints for student
    path('student/attendance-history/data/', views.student_attendance_history_data,
         name='student_attendance_history_data'),
    path('student/statistics/data/', views.student_statistics_data, name='student_statistics_data'),
    path('student/notifications/data/', views.student_notifications_data, name='student_notifications_data'),

]

