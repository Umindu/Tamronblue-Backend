from django.db import models

# Create your models here.
class Salary(models.Model):
    agent_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    month_of_year = models.DateField()
    monthly_income = models.DecimalField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agent_id