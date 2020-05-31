from django.db import models

# Create your models here.

class Expense(models.Model):
    # id will be automatically genearted
    expense_name = models.CharField(max_length=100,blank=False, null=False)
    expense_amount = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return(f"Expense {expense_name} was of amount {expense_amount}")