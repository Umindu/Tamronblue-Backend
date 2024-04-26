from rest_framework import permissions, generics
from .models import Variety
from .permissions import IsAdmin
from .serializers import VarietySerializer

# get all varieties
class VarietyList(generics.ListAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticated]

# get a specific variety
class VarietyDetail(generics.RetrieveAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticated]

# Admin only
# save the variety
class VarietyCreate(generics.CreateAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [IsAdmin]

# update the variety
class VarietyUpdate(generics.UpdateAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [IsAdmin]

# delete the variety
class VarietyDelete(generics.DestroyAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [IsAdmin]