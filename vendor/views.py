from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorSerializer


class VendorListCreateAPIView(APIView):

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)