from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Contacts


@receiver(post_migrate)
def create_contact(sender,**kwargs):
     if sender.name == 'apps.contacts':
        if Contacts.objects.all().exists():
            pass
        else:
            Contacts.objects.create(address='Some address',
                                facebook="facebook.com",
                                instagram="instagram.com",
                                phone_number="+996555000000",
                                whatsapp_number="+996555000000",
                                email="example@gmail.com")
            
