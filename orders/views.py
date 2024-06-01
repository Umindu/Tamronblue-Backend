from rest_framework import permissions, generics
from .models import Order, OrderItem, Payment
from .permissions import IsAdmin, IsAdminOrIsAgent, IsAgent
from .serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer


# Order...........................................
# Admin only
# get all orders
class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]

# delete the order
class OrderDelete(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]

# Admin and Agent only
# get my all orders
class OrderListByAgent(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrIsAgent]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(agent=user)

# get a specific order
class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrIsAgent]

# save the order
class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrIsAgent]

# update the order
class OrderUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrIsAgent]



# Order Item...........................................
# Admin only
# get all order items
class OrderItemList(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdmin]

# delete the order item
class OrderItemDelete(generics.DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdmin]

# Admin and Agent only
# get a specific order item
class OrderItemDetail(generics.RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminOrIsAgent]

# save the order item
class OrderItemCreate(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminOrIsAgent]

# update the order item
class OrderItemUpdate(generics.UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminOrIsAgent]



# Payment...........................................
# Admin only
# get all payments
class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdmin]

# delete the payment
class PaymentDelete(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdmin]

# get a specific payment
class PaymentDetail(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdmin]

# save the payment
class PaymentCreate(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdmin]

# update the payment
class PaymentUpdate(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdmin]