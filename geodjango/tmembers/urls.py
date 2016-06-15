from django.conf.urls import url, include
from django.contrib import admin
import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	#url(r'^accounts/profile', views.profile, name='profile'),
    url(r'^accounts/profile', views.edit_user, name='profile'),


]