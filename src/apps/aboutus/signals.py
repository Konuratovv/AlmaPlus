from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import AboutUsMainPage


@receiver(post_migrate)
def create_contact(sender,**kwargs):
     if sender.name == 'apps.aboutus':
        if AboutUsMainPage.objects.all().exists():
            pass
        else:
            AboutUsMainPage.objects.create(
                image=None,
                description='Company "Alma Pluse" has a successful history in the Oil & Gas industry. Company "Alma Pluse" has solid experience in the Kyrgyzstan market, where it has been present since 2015. Due to its history, Company "Alma Pluse" possesses extensive knowledge of the Oil & Gas industry, ranging from maintenance to spare parts supply, including on-field troubleshooting.' 
            )
            
