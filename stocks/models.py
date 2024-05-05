from django.db import models

# Create your models here.
class Stock(models.Model):
    plant_id = models.ForeignKey('plants.Plant', on_delete=models.CASCADE)
    variety_id = models.ForeignKey('varieties.Variety', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.plant_id} - {self.variety_id} - {self.quantity} - {self.price} - {self.date} - {self.description} - {self.created_at} - {self.updated_at}'