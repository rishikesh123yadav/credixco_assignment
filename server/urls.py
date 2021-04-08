from django.urls import path
from server import views
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from .models import Student,SuperAdmin,Teacher

admin.site.register(Student)
admin.site.register(SuperAdmin)
admin.site.register(Teacher)

urlpatterns = [
    path('student/', views.StudentDetails.as_view(), name='student'),
    path('student/signup', views.StudentCreate.as_view(), name='student_signup'),
    path('teacher/signup', views.TeacherCreate.as_view(), name='teacher_signup'),
    path('admin/signup', views.SuperAdminCreate.as_view(), name='admin_signup'),
    path('api/token/', views.AuthView.as_view(), name='token_obtain_pair'),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]