from django.db import models

from apps.common.models import BaseModel

# Create your models here.


class PlastPipesCategory(BaseModel):
    title = models.CharField(max_length=250, verbose_name='Name')

    class Meta:
        verbose_name = "Plast pipe's category"
        verbose_name_plural = "Plast pipe's categories"

    def __str__(self) -> str:
        return self.title
    

class PlastPipe(BaseModel):
    image = models.ImageField(upload_to='plast-pipes/', verbose_name='image')
    description = models.TextField(verbose_name='Text')
    category = models.ForeignKey(PlastPipesCategory, verbose_name="category", on_delete=models.CASCADE, related_name='pipes')

    class Meta:
        verbose_name = 'Plast pipe'
        verbose_name_plural = 'Plast pipes'

    
    def __str__(self) -> str:
        return self.description
    