from django.contrib import admin
from django.http import HttpRequest

from apps.common.common_fields import COMMON_FIELDS

from . import models

# Register your models here.


class EngineeringInline(admin.StackedInline):
    model = models.Engineering
    extra = 1


@admin.register(models.EngineeringCategory)
class EngineeringCategoryAdmin(admin.ModelAdmin):
    inlines = (EngineeringInline, )
    fields = (
        'title',
        *COMMON_FIELDS,
    )
    readonly_fields = (*COMMON_FIELDS, )
    list_display = ('title', *COMMON_FIELDS)


@admin.register(models.Engineering)
class EngineeringAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'description',
        *COMMON_FIELDS,
    )
    readonly_fields = (*COMMON_FIELDS, )
    list_display = ('title', *COMMON_FIELDS, )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

