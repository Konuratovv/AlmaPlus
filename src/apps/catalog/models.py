from django.db import models

from apps.common.models import BaseModel

# Create your models here.


class Catalog(BaseModel):
    image = models.ImageField(upload_to='catalog/', verbose_name='Image')
    title = models.CharField(max_length=250, verbose_name='Name')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Catalog'

    def __str__(self) -> str:
        return f'{self.title}'

