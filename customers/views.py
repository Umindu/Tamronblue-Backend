from rest_framework import permissions, generics
from .models import Customer
from .permissions import IsAdmin, IsAgent, IsAdminOrIsAgent
from .serializers import CustomerSerializer

# get all Customers
class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrIsAgent]

class CustomerListByAgent(generics.ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrIsAgent]

    def get_queryset(self):
        agent = self.request.user
        return Customer.objects.filter(agent_id=agent.id)

# get a specific Customer
class CustomerDetail(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrIsAgent]

# save the Customer
class CustomerCreate(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrIsAgent]

# Admin only
# update the Customer
class CustomerUpdate(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdmin]

# delete the Customer
class CustomerDelete(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdmin]