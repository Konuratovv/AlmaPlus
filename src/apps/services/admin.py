from django.contrib import admin
from . import models

# Register your models here.

class ServiceInline(admin.StackedInline):
    model = models.Service
    extra = 1


@admin.register(models.ServiceCategory)
class CategoryServiceAdmin(admin.ModelAdmin):
    fields = ('title', 'created_at', 'updated_at', )
    readonly_fields = ('created_at', 'updated_at', )
    inlines = (ServiceInline, )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ('text', 'category', 'created_at', 'updated_at', )
    readonly_fields = ('created_at', 'updated_at', )