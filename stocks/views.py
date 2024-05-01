from rest_framework import permissions, generics
from .models import Stock
from .permissions import IsAdmin, IsAdminOrIsAgent, IsAgent
from .serializers import StockSerializer

# get all Stock
class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

# get a specific Stock
class StockDetail(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

# Admin only
# save the Stock
class StockCreate(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdmin]

# update the Stock
class StockUpdate(generics.UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdmin]

# delete the Stock
class StockDelete(generics.DestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdmin]

