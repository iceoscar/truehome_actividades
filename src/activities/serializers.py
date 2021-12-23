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


class SurverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survery
        fields = '__all__'
