from django.db import models

# Create your models here.
class LandPlant(models.Model):
    land_id = models.ForeignKey('lands.Land', on_delete=models.CASCADE, null=True)
    plant_id = models.ForeignKey('plants.Plant', on_delete=models.CASCADE, null=True)
    variety_id = models.ForeignKey('varieties.Variety', on_delete=models.CASCADE, null=True)
    requirements_for_monthly = models.IntegerField(default=0)
    requirements_for_annual = models.IntegerField(default=0)

    def __str__(self):
        return  self.land_id.name +' '+ self.plant_id.name