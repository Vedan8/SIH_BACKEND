from .models import Vessels
from .serializers import VesselSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import Response,APIView

class AddVessel(ListAPIView):
    queryset=Vessels.objects.all()
    serializer_class=VesselSerializer

class VesselCount(APIView):
    def get(self,request):
        count=Vessels.objects.count()
        return Response({"VesselCount":count})

