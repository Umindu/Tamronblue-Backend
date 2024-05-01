from rest_framework import permissions, generics
from .models import LandPlant
from .permissions import IsAdmin, IsAdminOrIsAgent, IsAgent
from .serializers import LandPlantSerializer

# get all Lands and Plants
class LandPlantList(generics.ListAPIView):
    queryset = LandPlant.objects.all()
    serializer_class = LandPlantSerializer
    permission_classes = [permissions.IsAuthenticated]

# get a specific Land and Plant
class LandPlantDetail(generics.RetrieveAPIView):
    queryset = LandPlant.objects.all()
    serializer_class = LandPlantSerializer
    permission_classes = [permissions.IsAuthenticated]

# Admin only
# save the Land and Plant
class LandPlantCreate(generics.CreateAPIView):
    queryset = LandPlant.objects.all()
    serializer_class = LandPlantSerializer
    permission_classes = [IsAdmin]

# update the Land and Plant
class LandPlantUpdate(generics.UpdateAPIView):
    queryset = LandPlant.objects.all()
    serializer_class = LandPlantSerializer
    permission_classes = [IsAdmin]

# delete the Land and Plant
class LandPlantDelete(generics.DestroyAPIView):
    queryset = LandPlant.objects.all()
    serializer_class = LandPlantSerializer
    permission_classes = [IsAdmin]

