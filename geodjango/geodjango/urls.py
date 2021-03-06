"""geodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import web
#from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
##from registration.backends.simple.views import *#RegistrationView    
##from django.core.urlresolvers import reverse
##import userena
## class MyRegistrationView(RegistrationView):
##         def get_success_url(self, request, user):
##             return '/rango/'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^checkin/', web.checkin, name='checkin'),
	url(r'^register/', web.register),
	url(r'^home', web.home, name='home'),
    url(r'^$', web.home, name='home'),
    url(r'^about/', web.about, name='about'),
    url(r'^contact/', web.contact, name='contact'),
    url(r'^map/', web.MapListView.as_view(), name='map'),
    url(r'^directory/', web.DirectoryListView.as_view(), name='directory'),
    url(r'^accounts/', include('allauth.urls')),
    ##url(r'^accounts/profile', views.profile, name='profile'),
    ##url(r'^accounts/profile', views.edit_user, name='profile'),
    url(r'^accounts/', include('members.urls')),


    #url(r'^accounts/', include("userena.urls")),
    #url(r'^signup/', include('userena.urls')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









