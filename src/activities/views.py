from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

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


class SurveryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Survery.objects.all()
    serializer_class = SurverySerializer
    permission_classes = [permissions.IsAuthenticated]
