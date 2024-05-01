from django import forms
from listings.models import Band, Listings

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
   class Meta:
      model = Band
      exclude = ('active', 'official_homepage')  

class ListingsForm(forms.ModelForm):
   class Meta:
      model = Listings
      fields = '__all__' 
