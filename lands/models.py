from django.db import models

# Create your models here.
class Land(models.Model):
    name = models.CharField(max_length=100, default='')
    customer_id = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=300, default='')
    area = models.FloatField(default=0)
    district = models.CharField(max_length=100, default='')
    agricultural_zone = models.CharField(max_length=100, default='')
    density_of_cultivation = models.CharField(max_length=100, default='')
    acclimatization = models.CharField(max_length=100, default='')
    region = models.CharField(max_length=100, default='')
    requirements_for_monthly = models.IntegerField(default=0)
    requirements_for_annual = models.IntegerField(default=0)
    description = models.TextField(default='')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name