from rest_framework import serializers

from . import models 


class WorkScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.WorkSchedule
        fields = (
            'start_day',
            'end_day',
            'start_time',
            'end_time'
        )
        

class ContactsSerializer(serializers.ModelSerializer):
    work_schedule = WorkScheduleSerializer(many=True)

    class Meta:
        model = models.Contacts
        fields = (
            'address',
            'facebook',
            'instagram',
            'phone_number',
            'whatsapp_number',
            'email',
            'work_schedule',
        )