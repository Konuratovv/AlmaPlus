from django.db import models
from apps.common.models import BaseModel

# Create your models here.


class ServiceCategory(BaseModel):
    title = models.CharField(
        max_length=250,
        verbose_name='Name', 
    ) 


    class Meta:
        verbose_name = 'Category for services'
        verbose_name_plural = 'Categories for services'

    def __str__(self) -> str:
        return self.title
    

class Service(BaseModel):
    text = models.TextField(verbose_name='Text for services')
    category = models.ForeignKey(ServiceCategory, 
                                 on_delete=models.CASCADE, 
                                 related_name='services', 
                                 verbose_name='category')


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return f"service {self.text}"