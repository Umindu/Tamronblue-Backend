from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, default='')
    nic = models.CharField(max_length=12, default='')
    email = models.EmailField(max_length=255, unique=True,)
    phone = models.CharField(max_length=10, default='')
    address = models.TextField(default='')
    city = models.CharField(max_length=255, default='')
    counrty = models.CharField(max_length=255, default='')
    zip_code = models.CharField(max_length=10, default='')
    branch_id = models.ForeignKey('branches.Branch', on_delete=models.CASCADE, default=1)
    agent_id = models.ForeignKey('account.User', on_delete=models.CASCADE, default=1)
    staus = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name