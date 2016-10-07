from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
   
    def __str__(self):
        return self.name
