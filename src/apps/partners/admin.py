from django.contrib import admin

from apps.common.common_fields import COMMON_FIELDS

from . import models

# Register your models here.

@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    fields = ('title', *COMMON_FIELDS)
    readonly_fields = (*COMMON_FIELDS, )
    