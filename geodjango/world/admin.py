from django.contrib.gis import admin
from models import Member
# Register your models here.
admin.site.register(Member, admin.GeoModelAdmin)