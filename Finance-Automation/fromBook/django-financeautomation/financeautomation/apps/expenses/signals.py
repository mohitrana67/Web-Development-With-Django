from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.conf import settings

from .models import NewExpense

@receiver(expense_save,sender=NewExpense)
def expense_save_handler(sender, **kwargs):
    if settings.DEBUG:
        pring(f"{kwargs['instance']} saved.")

@receiver(expense_delete, sender=NewExpense)
def expense_delete_handler(sender, **kwargs):
    if settings.DEBUG:
        print(f"{kwargs['instance']} deleted")