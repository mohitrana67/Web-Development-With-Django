from rest_framework import serializers

from expenses.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            "user",
            "expense_name",
            "expense_invoice_date",
            "expense_paid_date",
            "expense_paid",
            "expense_reason",
            "is_recurring",
            "recurrsion_duration",
            "expense_amount",
            "expense_generated_currency",
            "expense_paid_currency"
        ]
    
    def create(self, validate_data):
        """
            Create and return a new instance, goven the validated data
        """

        return Expense.objects.create(**validate_data)