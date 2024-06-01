from rest_framework import permissions, generics
from .models import Land
from .permissions import IsAdmin, IsAdminOrIsAgent, IsAgent
from .serializers import LandSerializer

# get all lands
class LandList(generics.ListAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [IsAdminOrIsAgent]

# get a specific land
class LandDetail(generics.RetrieveAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [IsAdminOrIsAgent]

# land get by customer id
class LandByCustomer(generics.ListAPIView):
    serializer_class = LandSerializer
    permission_classes = [IsAdminOrIsAgent]

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Land.objects.filter(customer_id=customer_id)
    
# land get by agent id
class LandListByAgent(generics.ListAPIView):
    serializer_class = LandSerializer
    permission_classes = [IsAdminOrIsAgent]

    def get_queryset(self):
        agent_id = self.request.user
        return Land.objects.filter(agent_id=agent_id)

# save the land
class LandCreate(generics.CreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [IsAdminOrIsAgent]

# Admin only
# update the land
class LandUpdate(generics.UpdateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [IsAdmin]

# delete the land
class LandDelete(generics.DestroyAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [IsAdmin]
