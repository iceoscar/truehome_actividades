from datetime import timedelta

from rest_framework import serializers

from .models import Property, Activity, Survery


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and hasattr(self.instance, 'status'):
            for field in self.fields:
                self.fields[field].read_only = True
                if field == 'schedule' or field == 'property':
                    self.fields[field].read_only = False

    def validate(self, data):
        one_hour_before = data['schedule'] - timedelta(hours=1)
        one_hour_after = data['schedule'] + timedelta(hours=1)

        activities = Activity.objects.filter(
            property=data['property']
        ).filter(
            schedule__lt=one_hour_after,
            schedule__gt=one_hour_before
        )

        if self.instance:
            activities = activities.exclude(pk=self.instance.pk)

        # Verifica que la propiedad este activa
        if data['property'].status == Property.STATUS_DEACTIVATED:
            raise serializers.ValidationError({'property': 'No se puede dar de alta una actividad en una propiedad desactivada.'})
        # Verifica que no haya otra actividad cerca del mismo hroario
        if activities.count():
            raise serializers.ValidationError({'schedule': 'No se puede dar de alta una actividad en esta propiedad en esta fecha y hora por que ya hay una actividad asignada.'})
        # Verifica si la actividad esta cancelada
        if hasattr(self, 'instance') and hasattr(self.instance, 'status') and self.instance.status == Activity.STATUS_CANCELLED:
            raise serializers.ValidationError({'status': 'No se puede reagendar la actividad debido a que se encuentra cancelada.'})

        return data


class SurverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survery
        fields = '__all__'
