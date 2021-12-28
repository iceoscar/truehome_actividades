from django.urls import include, path
from rest_framework import routers

from .views import PropertyViewSet, ActivityViewSet, SurveryViewSet


# app_name = 'activities'

router = routers.DefaultRouter()
router.register(r'propiedades', PropertyViewSet)
router.register(r'actividades', ActivityViewSet)
router.register(r'encuestas', SurveryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
