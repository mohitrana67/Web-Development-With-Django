from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.conf import settings

from .models import NewArticle

@receiver(post_save,sender=NewArticle)
def news_save_handler(sender, **kwargs):
    if settings.DEBUG:
        print(f"{kwargs['instance']} saved.")

@receiver(post_delete,sender=NewArticle)
def news_delete_handler(sender, **kwargs):
    if settings.DEBUG:
        print(f"{kwargs['instance']} deleted.")