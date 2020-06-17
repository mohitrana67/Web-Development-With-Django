from django import forms

from .models import *

class AddExpense(forms.ModelForm):

    class Meta:
        model = Expense
        fields = [
                    'expense_account_type',
                    'expense_transaction_date',
                    'expense_name',
                    'expense_description_1',
                    'expense_description_2',
                    'expense_amount_cad',
                    'expense_amount_usd',
                    'expense_gst',
                    'expense_pst',
                    'expense_pvt'
                ]
        
    def clean_content(self):
        # We will check what we are getting in the form and we will do the validations here
        pass