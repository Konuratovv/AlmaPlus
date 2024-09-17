from django.db import models
from apps.common.models import BaseModel

# Create your models here.


class Contacts(BaseModel):
    address = models.TextField(verbose_name='Address')
    facebook = models.URLField(verbose_name='Facebook')
    instagram = models.URLField(verbose_name='instagram')
    phone_number = models.CharField(max_length=50, verbose_name='Phone Number')
    whatsapp_number = models.CharField(max_length=50, verbose_name='Whatsapp number')
    email = models.EmailField(verbose_name='email')

    class Meta:
        verbose_name = 'Contact'
        verbose_name = 'Contacts'

    
    def __str__(self) -> str:
        return 'Contact'


class WorkSchedule(BaseModel):
    DAY_CHOICES = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednessday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )

    start_day = models.CharField(max_length=30, choices=DAY_CHOICES, verbose_name='Start day')
    end_day = models.CharField(max_length=30, choices=DAY_CHOICES, verbose_name='End day')
    start_time = models.TimeField(verbose_name='Start time')
    end_time = models.TimeField(verbose_name='End time')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, related_name='work_schedule', verbose_name='Contacts')

    class Meta:
        verbose_name = 'Work Schedule'

    
    def __str__(self) -> str:
        return f'{self.start_day} - {self.end_day}, {self.start_time} - {self.end_time}'
    


