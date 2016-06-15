from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from members.models import UserProfile
from .models import UserProfile
from .forms import UserForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response, render
from django.views import generic
from django.template import RequestContext
from geopy.geocoders import GoogleV3
#from geopy.geocoders.googlev3 import GQueryError
from urllib2 import URLError
from django.contrib.gis import geos
from django.contrib.gis import measure



@login_required() # only logged in users should access this
def edit_user(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)
 
    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)
 
    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('name','avatar', 'website', 'bio', 'phone', 'street_address', 'city', 'country'))
    formset = ProfileInlineFormset(instance=user)
 
    if request.user.is_authenticated() and request.user.id == user.id:
    	print "is_authenticated"
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    print "formset save"
                    path = "/accounts/profile/{pk}"
                    fpath = path.format(pk=request.user.user.user_id)
                    print fpath
                    return HttpResponseRedirect(fpath) #('/accounts/profile/')

 
        return render(request, "members/account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

# def profile(request):
# 	return render_to_response("members/profile.html", locals())

class ProfileDetailView(generic.DetailView):
	model = User
	template_name = 'members/profile.html'

def geocode_address(address):
    address = address.encode('utf-8')
    geocoder = GoogleV3()
    try:
        _, latlon = geocoder.geocode(address)
    except (URLError, ValueError):
        return None
    else:
        return latlon


