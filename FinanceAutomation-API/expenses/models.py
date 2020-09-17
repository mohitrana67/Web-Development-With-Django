from django.db import models
from accounts.models import Account

# Create your models here.
class Expense(models.Model):
    recurssion_durations = [
        ("SW", "Weekly"),
        ("BW", "Bi-Weekly"),
        ("M", "Monthly"),
        ("Y", "Yearly"),
        ("S", "Single Time")
    ]
    currencies = [
        ("USD", "United States Dollars"),
        ("CAD", "Canadian Dollars")
    ]
    user = models.ForeignKey(Account, verbose_name='Name of the user who enters the data', on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=255, verbose_name='Name of the expense', blank=False)
    expense_invoice_date = models.DateField(verbose_name='Date invoice for the expense was generated', blank=False)
    expense_paid_date = models.DateField(verbose_name='Date expense was paid', blank=True)
    expense_paid = models.BooleanField(default=False, verbose_name='If expense is paid or not')
    expense_reason = models.CharField(max_length=255, verbose_name='Description about the expense', blank=False)
    is_reccuring = models.BooleanField(default=False, verbose_name='Is expense reccuring every week, month or year')
    recurrsion_duration = models.CharField(max_length=2, choices=recurssion_durations, verbose_name="Reccuring Frequency")
    expense_amount = models.IntegerField(blank = False, verbose_name='Totals Amount of the expense')
    expense_generated_currency = models.CharField(max_length=3, choices = currencies, verbose_name="Currency in whicih expense was generated", blank=False)
    expense_paid_currency = models.CharField(max_length=3, choices = currencies, verbose_name="Currency in which expense was paid", blank=False)

    def __str__(self):
        return f"{expense_name} was added by {user}"