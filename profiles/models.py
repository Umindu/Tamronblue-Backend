from django.db import models

# Create your models here.
class Profile(models.Model):
    user_id = models.ForeignKey('account.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(verbose_name='Email',max_length=255)
    nic = models.CharField(max_length=12, default='')
    gender = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=12, default='')
    address = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    postal_code = models.CharField(max_length=255, default='')
    point = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    monthly_income = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    sold_plant_count = models.IntegerField(default=0)
    is_admin=models.BooleanField(default=False)
    is_agent=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name