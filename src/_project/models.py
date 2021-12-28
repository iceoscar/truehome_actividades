from django.db import models


class BaseModel(models.Model):
	STATUS_ACTIVE = 'active'
	STATUS_DEACTIVATED = 'deactivated'
	STATUS_CANCELLED = 'cancelled'
	STATUS_RESCHEDULED = 'rescheduled'
	STATUS_DONE = 'done'

	CHOICES_STATUS = (
		(STATUS_ACTIVE, 'Activo'),
		(STATUS_DEACTIVATED, 'Inactivo'),
		(STATUS_CANCELLED, 'Cancelado'),
		(STATUS_RESCHEDULED, 'Re-agendado'),
		(STATUS_DONE, 'Finalizada'),
	)

	class Meta:
		abstract = True

	title = models.CharField('Nombre', max_length=255)
	status = models.CharField('Estatus', max_length=35, choices=CHOICES_STATUS, default=STATUS_ACTIVE)

	def __str__(self):
		return '{}'.format(self.title)


class TimeStampModel(models.Model):
	class Meta:
		abstract = True

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
