from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    

        name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                'placeholder': '메뉴 이름을 작성해 주세요.',
                'class': 'form-control',
            })
        )

        price = forms.DecimalField(
            max_digits=8,
            decimal_places=2,
            error_messages={
                'invalid': '올바른 가격을 입력해 주세요. 예: 12.34',
                'max_digits': '가격은 최대 8자리여야 합니다.',
                'max_decimal_places': '가격은 소수점 이하 두 자리여야 합니다.',
            },
            widget=forms.NumberInput(
                attrs={
                'placeholder': '숫자만 입력 가능합니다.',
                'class': 'form-control',
            })
        )

        description = forms.CharField(
            widget=forms.Textarea(
                attrs={
                'placeholder': '메뉴 설명을 작성해 주세요.',
                'class': 'form-control',
                'rows': 5
            })
        )

        is_vegan = forms.ChoiceField(
            choices=[(True, 'Yes'), (False, 'No')],
            widget=forms.RadioSelect(
                attrs={
                'class': 'form-check-input'
            })
        )
        class Meta:
            model = Menu
            fields = '__all__'