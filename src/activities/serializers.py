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

    def validate(self, data):
        one_hour_before = data['schedule'] - timedelta(hours=1)
        one_hour_after = data['schedule'] + timedelta(hours=1)

        activities = Activity.objects.filter(property=data['property']).exclude(schedule__range=[one_hour_before,one_hour_after])
        if self.instance:
            activities = activities.exclude(pk=self.instance.pk)

        # Verifica que la propiedad este activa
        if data['property'].status == Property.STATUS_DEACTIVATED:
            raise serializers.ValidationError({'property': 'No se puede dar de alta una actividad en una propiedad desactivada.'})
        # Verifica que no haya otra actividad cerca del mismo hroario
        if activities.count():
            raise serializers.ValidationError({'schedule': 'No se puede dar de alta una actividad en esta propiedad en esta fecha y hora por que ya hay una actividad asignada.'})
        return data


class SurverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survery
        fields = '__all__'
