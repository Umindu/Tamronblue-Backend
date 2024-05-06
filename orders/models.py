from django.db import models

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='orders')
    Agent = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='orders')
    land = models.ForeignKey('lands.Land', on_delete=models.CASCADE, related_name='orders')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='Pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE, related_name='order_items')
    variety = models.ForeignKey('varieties.Variety', on_delete=models.CASCADE, related_name='order_items')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)