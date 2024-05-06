from django.db import models

# Create your models here.
class GrnDetail(models.Model):
    grn_date = models.DateField()
    # supplier_id = models.ForeignKey('suppliers.Supplier', on_delete=models.CASCADE)
    # invoice_no = models.CharField(max_length=50)
    # invoice_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_tax = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
class Grn(models.Model):
    grn_id = models.ForeignKey('GrnDetail', on_delete=models.CASCADE)
    plant_id = models.ForeignKey('plants.Plant', on_delete=models.CASCADE)
    variety_id = models.ForeignKey('varieties.Variety', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total_tax = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
