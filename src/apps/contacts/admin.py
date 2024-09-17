from django.contrib import admin
from django.http.request import HttpRequest

from . import models

# Register your models here.


@admin.register(models.WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    pass

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    


class WorkScheduleInline(admin.StackedInline):
    model = models.WorkSchedule
    extra = 1
    max_num = 1

@admin.register(models.Contacts)
class ContactsAdmin(admin.ModelAdmin):
    inlines = (WorkScheduleInline, )
    fields = ('address', 
              'facebook', 
              'instagram',
              'phone_number',
              'whatsapp_number',
              'email',
              'created_at',
              'updated_at', )
    list_display = (
        'id',
        'address',
        'email',
        'phone_number',
        'whatsapp_number',
        'created_at',
    )
    readonly_fields = ('created_at', 'updated_at', )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
