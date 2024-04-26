from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=300, default='')
    district = models.CharField(max_length=100, default='')
    agricultural_zone = models.CharField(max_length=100, default='')
    region = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name