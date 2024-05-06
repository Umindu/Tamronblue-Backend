from django.db import models

# Create your models here.
class Salary(models.Model):
    agent_id = models.ForeignKey('account.User', on_delete=models.CASCADE)
    month_of_year = models.DateField()
    monthly_income = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agent_id