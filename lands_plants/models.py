from django.db import models

# Create your models here.
class LandPlant(models.Model):
    land_id = models.ForeignKey('lands.Land', on_delete=models.CASCADE, null=True)
    plant_id = models.ForeignKey('plants.Plant', on_delete=models.CASCADE, null=True)
    variety_id = models.ForeignKey('varieties.Variety', on_delete=models.CASCADE, null=True)
    plant_quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.land_id