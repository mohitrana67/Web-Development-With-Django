from django import forms

from .models import *

class AddTripForm(forms.ModelForm):
     
    class Meta:
        model = Trip
        fields = ['trip_no','origin_city','destination_city']

    def clean_content(self):
        trip_no = self.cleaned_data.get("trip_no")
        origin_city = self.cleaned_data.get("origin_city")
        destination_city = self.cleaned_data.get("destination_city")