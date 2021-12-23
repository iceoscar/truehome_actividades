from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Property, Activity, Survery
from .serializers import PropertySerializer, ActivitySerializer, SurverySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'], name='Cancelar Actividad', permission_classes=[permissions.IsAuthenticated])
    def set_cancelled(self, request, pk=None):
        activity = self.get_object()
        activity.status = Activity.STATUS_CANCELLED
        activity.save()
        return Response({
            'activity': activity.title,
            'property': activity.property.title,
            'schedule': activity.schedule,
            'msg': 'Actividad Cancelada'
        })


class SurveryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Survery.objects.all()
    serializer_class = SurverySerializer
    permission_classes = [permissions.IsAuthenticated]
