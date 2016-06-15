from django.conf.urls import url, include
from django.contrib import admin
import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	#url(r'^profile', views.profile, name='profile'),
	url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name='profile'),
    url(r'^account_update/(?P<pk>\d+)/$', views.edit_user, name='update'),
    	#(?P<pk>\d+)/$', views.edit_user, name='profile'),
]