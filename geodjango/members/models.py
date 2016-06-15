from __future__ import unicode_literals
from urllib2 import URLError
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.db import models
from geopy.geocoders import GoogleV3
#from geopy.geocoders.googlev3 import GQueryError
from django.db.models.signals import post_save
from django.forms import ModelForm
#from django.contrib.gis.db.models import PointField, GeoManager
import geodjango.settings

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name=_('user'), on_delete=models.CASCADE)
	name = models.CharField(max_length=500, default='', blank=True)
	avatar = models.ImageField(upload_to = 'img/usrpics/', null=True, blank=True, default="/img/dog.png")
	street_address = models.CharField(max_length=200,default='', blank=True)
	city = models.CharField(max_length=100,default='', blank=True)
	state = models.CharField(max_length=100, null=True)
	postal_code = models.CharField(max_length=100, null=True)
	country = models.CharField(max_length=100, default='', blank=True)
	website = models.URLField(default='', blank=True)
	phone = models.CharField(max_length=20, blank=True, default='')
	BUSINESS = 'BUS'
	ORGANIZATION = 'ORG'
	RESIDENT = 'RES'
	OTHER = 'OTH'
	BUS_ORG_RES_CHOICES = (
	(BUSINESS, 'Business'),
	(ORGANIZATION, 'Organization'),
	(RESIDENT, 'Resident'),
	(OTHER, 'Other'),
	)
	user_com_status = models.CharField(max_length=3,choices=BUS_ORG_RES_CHOICES, default=RESIDENT )
	bio = models.TextField(default='', blank=True)
    #point = PointField()
	#objects = GeoManager()
	location = gis_models.PointField(u"longitude/latitude",
                                     geography=True, blank=True, null=True)
	gis = gis_models.GeoManager()
	objects = models.Manager()

# Returns the string representation of the model.
	def __unicode__(self):
		return self.name


	def save(self, **kwargs):
		if (not self.location) or self.location:
			address = u'%s %s %s %s' % (self.street_address, self.city, self.state, self.postal_code)
			address = address.encode('utf-8')
			geocoder = GoogleV3()
			try:
				_, latlon = geocoder.geocode(address)
			except (URLError, ValueError):
				pass
			else:
				point = "POINT(%s %s)" % (latlon[1], latlon[0])
				self.location = geos.fromstr(point)
		super(UserProfile, self).save()

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

    