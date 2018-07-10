from django.db import models

# Create your models here.

class Paddler(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    generation = models.IntegerField(default=0)
    major = models.CharField(max_length=50)
    year = models.IntegerField(default=0)

    def __str__(self):
        display_name = str(self.first_name) + ' ' + str(self.last_name)
        return display_name

