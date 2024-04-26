from django.db import models

# Create your models here.
class Variety(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    plant_id = models.ForeignKey('plants.Plant', on_delete=models.CASCADE, default=2)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

# json
# {
#     "name": "Variety 1",
#     "description": "This is a variety",
#     "plant_id": 1,
#     "status": true
# }