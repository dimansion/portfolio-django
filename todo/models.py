from django.db import models
from django.utils import timezone
# Create your models here.

class Jadwal(models.Model):
	kegiatan = models.CharField(max_length=120)
	waktu = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.kegiatan