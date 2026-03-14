from django.urls import path
from .views import VendorProductMappingAPIView

urlpatterns = [
    path('vendor-products/', VendorProductMappingAPIView.as_view(), name='vendor-products'),
]