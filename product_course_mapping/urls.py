from django.urls import path
from .views import ProductCourseMappingAPIView

urlpatterns = [
    path('product-courses/', ProductCourseMappingAPIView.as_view(), name='product-courses'),
]