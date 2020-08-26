from rest_framework import serializers
from expenses.models import Expense

class ExpenseSerializer(serializers.Serializer):
    expense_name = serializers.CharField(required=True, max_length=255)
    expense_date = serializers.DateField(required=True)

    def create(self, validated_data):
        """
        Create and return a new 'expense' instance, given the validate data.
        """

        return Expense.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing 'Expense' instance, given the validated data.
        """

        instance.expense_name = validated_data.get('expense_name', instance.expense_name)
        instance.expense_date = validated_data.get('expense_date', instance.expense_date)

        instance.save()
        return instance