from django.db import models

from apps.common.models import BaseModel

# Create your models here.


class AboutUsMainPage(BaseModel):
    image = models.ImageField(upload_to='about-us-main-page/', verbose_name='Image')
    description = models.TextField(verbose_name='Text')

    class Meta:
        verbose_name = 'About Us on main page'

    def __str__(self) -> str:
        return self.description
    

class AboutUs(BaseModel):
    title = models.CharField(max_length=350, verbose_name='Name')
    description = models.TextField(verbose_name='Text')

    class Meta:
        verbose_name = 'About us on different page'

    def __str__(self) -> str:
        return self.title