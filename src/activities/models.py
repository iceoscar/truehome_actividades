from django.contrib.postgres.fields import JSONField
from django.db import models


from _project.models import BaseModel, TimeStampModel


class Property(BaseModel, TimeStampModel):
	class Meta:
		verbose_name = 'Propiedad'
		verbose_name_plural = 'Propiedades'

	address = models.TextField('Dirección')
	description = models.TextField('Descripción')
	disabled_at = models.DateTimeField('Inactivar', blank=True, null=True)


class Activity(BaseModel, TimeStampModel):
	class Meta:
		verbose_name = 'Actividad'
		verbose_name_plural = 'Actividades'

	property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='Propiedad')
	schedule = models.DateTimeField()


class Survery(TimeStampModel):
	class Meta:
		verbose_name = 'Encuesta'
		verbose_name_plural = 'Encuestas'

	activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='Actividad')
	answers = JSONField()

	def __str__(self):
		return 'Prop: {} - Actividad: {} ({})'.format(self.activity.property, self.activity, self.pk)
