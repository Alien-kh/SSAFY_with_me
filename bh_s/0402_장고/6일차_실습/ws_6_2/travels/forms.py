from django import forms
from .models import Travel


class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'
        widgets = {
            'location' : forms.TextInput(attrs={'placeholder' : 'ex)제주도'}),
            'plan' : forms.Textarea(attrs={'placeholder':'슉.슈슉.슈욱', 'cols': 30, 'rows':10}),
            'start_date' : forms.TextInput(attrs={'placeholder' : 'ex)2022-02-22'}),
            'end_date' : forms.TextInput(attrs={'placeholder' : 'ex)2022-02-22'}),
        }