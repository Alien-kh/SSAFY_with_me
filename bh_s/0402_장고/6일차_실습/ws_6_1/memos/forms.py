from django import forms
from .models import Memo


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = '__all__'
        widgets = {
            'summary': forms.TextInput(attrs={'placeholder': 'summary'}),
            'memo': forms.Textarea(attrs={'placeholder': 'memo', 'cols': 50, 'rows': 5}),
        }