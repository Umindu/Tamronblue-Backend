from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(verbose_name='Email',max_length=255)
    point = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    is_admin=models.BooleanField(default=False)
    is_agent=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name