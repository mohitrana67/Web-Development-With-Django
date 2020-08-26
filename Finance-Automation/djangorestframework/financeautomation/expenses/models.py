from django.db import models
import datetime
from users.models import User

# Create your models here.

class Expense(models.Model):
    expense_name = models.CharField(max_length=255, blank=False, null=False)
    expense_date = models.DateField(default=datetime.date.today,blank=False, null=False)
    
    class Meta:
        ordering = ['expense_date']