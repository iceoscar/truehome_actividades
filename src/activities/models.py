from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.db import models

from _project.models import BaseModel, TimeStampModel


class Property(BaseModel, TimeStampModel):
	class Meta:
		verbose_name = 'Propiedad'
		verbose_name_plural = 'Propiedades'

	address = models.TextField('Dirección')
	description = models.TextField('Descripción')
	disabled_at = models.DateTimeField('Inactivar', blank=True, null=True, help_text='Formato: aaaa-mm-dd HH:MM:SS')


class Activity(BaseModel, TimeStampModel):
	class Meta:
		verbose_name = 'Actividad'
		verbose_name_plural = 'Actividades'

	property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='Propiedad')
	schedule = models.DateTimeField('Calendario', help_text='Formato: aaaa-mm-dd HH:MM:SS')

	def get_condition(self):
		now = timezone.now()
		condition = self.get_status_display()
		if self.schedule < now and (self.status == self.STATUS_RESCHEDULED or self.status == self.STATUS_ACTIVE):
			condition = 'Atrasada'
		elif self.schedule >= now and (self.status == self.STATUS_RESCHEDULED or self.status == self.STATUS_ACTIVE):
			condition = 'Pendiente a realizar'
		return condition


class Survery(TimeStampModel):
	class Meta:
		verbose_name = 'Encuesta'
		verbose_name_plural = 'Encuestas'

	activity = models.OneToOneField(Activity, on_delete=models.CASCADE, verbose_name='Actividad')
	answers = JSONField()

	def __str__(self):
		return 'Prop: {} - Actividad: {} ({})'.format(self.activity.property, self.activity, self.pk)
