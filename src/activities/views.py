from datetime import date, timedelta
from django.shortcuts import render

from rest_framework import status, viewsets
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

    def get_queryset(self):
        qs = super().get_queryset()
        today = date.today()
        tree_days = today - timedelta(days=3)
        two_weeks = today + timedelta(weeks=2)
        qs = qs.filter(schedule__gte=tree_days, schedule__lte=two_weeks)
        return qs

    def list(self, request, *args, **kwargs):
        items = []
        for item in self.get_queryset():
            url_survery = '/encuesta/{}/'.format(item.survery.pk) if hasattr(item, 'survery') else None
            items.append({
                'id': item.pk,
                'schedule': item.schedule,
                'title': item.title,
                'created_at': item.created_at,
                'status': item.status,
                'condition': item.get_condition(),
                'property': {
                    'id': item.property.pk,
                    'title': item.property.title,
                    'address': item.property.address
                },
                'survery': url_survery
            })
        return Response(items)

    @action(detail=True, methods=['get'], name='Cancelar Actividad', permission_classes=[permissions.IsAuthenticated])
    def set_cancelled(self, request, pk=None):
        activity = self.get_object()
        activity.status = Activity.STATUS_CANCELLED
        activity.save()
        return Response({
            'activity': activity.title,
            'property': activity.property.title,
            'schedule': activity.schedule,
            'status': activity.get_status_display()
        })

    @action(detail=True, methods=['get'], name='Actividad Finalizada', permission_classes=[permissions.IsAuthenticated])
    def set_done(self, request, pk=None):
        activity = self.get_object()
        activity.status = Activity.STATUS_DONE
        activity.save()
        return Response({
            'activity': activity.title,
            'property': activity.property.title,
            'schedule': activity.schedule,
            'status': activity.get_status_display()
        })


class SurveryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Survery.objects.all()
    serializer_class = SurverySerializer
    permission_classes = [permissions.IsAuthenticated]
