# make sure this is at the top if it isn't already
from django import forms
# our new form

class SignupForm(forms.Form):
#class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='firstname')
    last_name = forms.CharField(max_length=30, label='lastname')
    #class Meta:
    #    model = Profile
    #    fields = ('first_name', 'last_name', 'address', 'city', 'state', 'zip', 'phone_number')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()



class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    
    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you think?"



