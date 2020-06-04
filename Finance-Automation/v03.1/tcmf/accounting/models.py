from django.db import models

# Create your models here.

class Expense(models.Model):
    # id will be automatically genearted
    expense_account_type = models.CharField(max_length=100,blank=False, null=False)
    expense_transaction_date = models.DateField(null=False, blank=False)
    expense_name = models.CharField(max_length=100,blank=False, null=False)
    expense_description_1 = models.CharField(max_length = 256, default='No Descriptiong Available')
    expense_description_2 = models.CharField(max_length = 256, default='No Descriptiong Available')
    expense_amount_cad = models.IntegerField(default = 0)
    expense_amount_usd = models.IntegerField(default = 0)
    expense_gst = models.IntegerField(default = 0)
    expense_pst = models.IntegerField(default = 0)
    expense_pvt = models.IntegerField(default = 0)