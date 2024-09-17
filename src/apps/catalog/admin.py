from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Catalog)
class CatalogAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'title',
        'description',
        'created_at',
        'updated_at',
    )
    readonly_fields = ('created_at', 'updated_at', )
    list_display = (
        'title',
        'created_at',
        'updated_at',
    )
