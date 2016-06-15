#-*- coding: utf-8 -*-
from django.http import *
from django import template
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import fromstr
from world.models import Member
import forms
from forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib.auth.models import User
from django.views import generic

def map(request):
    return render_to_response("map.html", locals())

class MapListView(generic.ListView):
    template_name = 'map.html'

    def get_queryset(self):
        return User.objects.all()


def checkin(request):
	return render_to_response("checkin.html", locals())

def home(request):
	return render_to_response("home0.html", locals())	

def about(request):
	return render_to_response("about.html", locals())

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form ",
                "Thank you for contacting us!",
                "northbucks19125@gmail.com",
                [contact_email])
            email.send()
            return HttpResponseRedirect('/')

    return render(request, 'contact.html', {
        'form': form_class,
    })

# def directory(request):
# 	return render_to_response("directory.html", locals())
class DirectoryListView(generic.ListView):
    template_name = 'directory.html'

    def get_queryset(self):
        return User.objects.all()


@csrf_exempt	
def register(request):
	if request.method == "POST":
		
		print request.POST.get("username")
		print request.POST.get("userimage")
		uname = request.POST.get("username")
		uimg = request.POST.get("userimage")
		ulong = request.POST.get("long")
		ulat = request.POST.get("lat")
		pnt = fromstr('POINT(%s %s)' % (ulat, ulong), srid=4326)
		print pnt

		newmember = Member(name=uname, image=uimg, point=pnt)
		newmember.save()

		return HttpResponse("welldone")
	else:
		return HttpResponse("Err.")