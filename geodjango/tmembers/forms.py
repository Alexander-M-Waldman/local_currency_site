# from members.models import UserProfile
# from django import forms


# class UserProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = UserProfile
# 		fields = ('name', 'phone_number', 'image', 'address', 'city', 'state', 'postal_code', 'country', 'user_com_status', )

# form = UserProfileForm()

from django import forms
from django.contrib.auth.models import User
 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']