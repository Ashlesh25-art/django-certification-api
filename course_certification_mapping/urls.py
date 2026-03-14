from django.urls import path
from .views import CourseCertificationMappingAPIView

urlpatterns = [
    path('course-certifications/', CourseCertificationMappingAPIView.as_view(), name='course-certifications'),
]