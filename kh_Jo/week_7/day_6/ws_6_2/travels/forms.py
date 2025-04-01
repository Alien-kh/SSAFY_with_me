from django import forms
from .models import Travels 

class TravelsForm(forms.ModelForm):
    class Meta:
        model = Travels
        fields = '__all__'
        widgets = {
            'location' : forms.TextInput(attrs={'placeholder': '제주도'}),
            'plan': forms.TextInput(attrs={'placeholder': 'ex) 슉, 슈슉.'}),
            'start_date' : forms.DateInput(attrs={'placeholder': 'ex)2022-02-22'}),
            'end_date' : forms.DateInput(attrs={'placeholder': 'ex)2022-02-22'})
        }