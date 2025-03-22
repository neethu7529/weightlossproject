from django import forms
from .models import WeightRegister

class AddWeightForm(forms.ModelForm):
    class Meta:
        model = WeightRegister
        fields = ['weight'] 
        


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))