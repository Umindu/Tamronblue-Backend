from rest_framework import permissions, generics
from .models import Branch
from .permissions import IsAdmin
from .serializers import PlantSerializer

# get all plants
class PlantList(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticated]

# get a specific plant
class PlantDetail(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticated]

# Admin only
# save the plant
class PlantCreate(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsAdmin]

# update the plant
class PlantUpdate(generics.UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsAdmin]

# delete the plant
class PlantDelete(generics.DestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsAdmin]