from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer

# Create your views here.
def all_api_paths(request):
    return JsonResponse(
        {"messages": "you are in api view"}
    )

# view for creating and listing expenses
@api_view(['GET','POST'])
def expense_list(request):
    """
    List all expenses or create a new expense.
    """
    if request.method == 'GET':
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view to list update and delete a single expense
@api_view(['GET', 'PUT', 'DELETE'])
def expense_detail(request, pk):
    """
    Retrieve, update or delete an individual expense.
    """
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
