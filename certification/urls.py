from django.urls import path
from .views import CertificationListCreateAPIView

urlpatterns = [
    path('certifications/', CertificationListCreateAPIView.as_view(), name='certifications'),
]