from django.db import models

# Create your models here.
class Expense(models.Model):
    # id will be automatically genearted
    expense_account_type = models.CharField(max_length=100,blank=False, null=False)
    expense_transaction_date = models.DateField(null=False, blank=False) # format is yyyy-mm-dd
    expense_name = models.CharField(max_length=100,blank=False, null=False)
    expense_description_1 = models.CharField(max_length = 256, default='No Descriptiong Available')
    expense_description_2 = models.CharField(max_length = 256, default='No Descriptiong Available')
    expense_amount_cad = models.IntegerField(default = 0)
    expense_amount_usd = models.IntegerField(default = 0)
    expense_gst = models.IntegerField(default = 0)
    expense_pst = models.IntegerField(default = 0)
    expense_pvt = models.IntegerField(default = 0)
    expense_quarter = models.IntegerField(default = 1)
    expense_year = models.IntegerField(default = 1000)
    docuemnt_type = models.CharField(max_length=256)

    def serialize(self):
        return {
            "id":self.id,
            "expense_account_type":self.expense_account_type,
            "expense_transaction_date":self.expense_transaction_date,
            "expense_name":self.expense_name,
            "expense_description_1":self.expense_description_1,
            "expense_description_2":self.expense_description_2,
            "expense_amount_cad":self.expense_amount_cad,
            "expense_amount_usd":self.expense_amount_usd,
            "expense_gst":self.expense_gst,
            "expense_pst":self.expense_pst,
            "expense_pvt":self.expense_pvt
        }