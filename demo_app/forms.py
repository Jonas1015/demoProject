from django import forms
from .models import ourData

# Create your forms here
class addRegionForm(forms.ModelForm):
    class Meta:
        model = ourData
        fields = ['region', 'population', 'number_of_district']
