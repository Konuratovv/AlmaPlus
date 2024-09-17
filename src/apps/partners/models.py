from django.db import models

from apps.common.models import BaseModel

# Create your models here.


class Partner(BaseModel):
    title = models.CharField(max_length=350, verbose_name='Partners')

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


    def __str__(self) -> str:
        return self.title