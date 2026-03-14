from django.urls import path
from .views import VendorListCreateAPIView

urlpatterns = [
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendors'),
]