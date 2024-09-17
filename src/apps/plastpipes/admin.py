from django.contrib import admin
from django.http import HttpRequest

from apps.common.common_fields import COMMON_FIELDS

from . import models

# Register your models here.


class PlastPipeInline(admin.StackedInline):
    model = models.PlastPipe
    extra = 1


@admin.register(models.PlastPipesCategory)
class PlastPipeCategoryAdmin(admin.ModelAdmin):
    inlines = (PlastPipeInline, )
    fields = (
        'title',
        *COMMON_FIELDS,
    )
    readonly_fields = (*COMMON_FIELDS, )
    list_display = ('title', *COMMON_FIELDS, )


@admin.register(models.PlastPipe)
class PlasticPipeAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'description',
        *COMMON_FIELDS,
    )
    readonly_fields = (*COMMON_FIELDS, )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False