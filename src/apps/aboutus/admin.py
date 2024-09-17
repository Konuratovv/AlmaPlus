from django.contrib import admin
from django.http import HttpRequest

from apps.common.common_fields import COMMON_FIELDS

from . import models

# Register your models here.

@admin.register(models.AboutUsMainPage)
class AboutUsOnMainPageAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'description',
        *COMMON_FIELDS,
    )
    list_display = ('description', *COMMON_FIELDS, )
    readonly_fields = (*COMMON_FIELDS, )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    
@admin.register(models.AboutUs)
class AboutUs(admin.ModelAdmin):
    fields = (
        'title',
        'description',
        *COMMON_FIELDS, 
    )
    readonly_fields = (*COMMON_FIELDS, )
    list_display = ('title', *COMMON_FIELDS, )

    

