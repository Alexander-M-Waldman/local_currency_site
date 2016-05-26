from __future__ import unicode_literals

#from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length=500)
	image = models.CharField(max_length=500)
	point = models.PointField()
	objects = models.GeoManager()

# Returns the string representation of the model.
	def __unicode__(self):
		return self.name
