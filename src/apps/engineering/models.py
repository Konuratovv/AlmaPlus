from django.db import models

from apps.common.models import BaseModel

# Create your models here.


class EngineeringCategory(BaseModel):
    title = models.CharField(max_length=350, verbose_name='Name')

    class Meta:
        verbose_name = 'Engineering category'
        verbose_name_plural = 'Engineering categories'

    def __str__(self) -> str:
        return self.title
    

class Engineering(BaseModel):
    title = models.CharField(max_length=350, verbose_name='Name')
    description = models.TextField(verbose_name='Text')
    category = models.ForeignKey(EngineeringCategory, on_delete=models.CASCADE, related_name='engineering', verbose_name='category')

    class Meta:
        verbose_name = 'Engineering'

    def __str__(self) -> str:
        return self.title