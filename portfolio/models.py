from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField()
	image = models.ImageField(null=True, blank=True)
	url = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.title

