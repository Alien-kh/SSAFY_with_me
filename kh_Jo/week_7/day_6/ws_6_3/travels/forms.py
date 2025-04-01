from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
    # price 필드를 오버라이딩하여 widget 속성을 설정합니다.
    price = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        error_messages={
            'invalid': '올바른 가격을 입력해 주세요. 예: 12.34',
            'max_digits': '가격은 최대 8자리여야 합니다.',
            'max_decimal_places': '가격은 소수점 이하 두 자리여야 합니다.',
        },
        widget=forms.TextInput(attrs={
            # 소수점 포함하여 최대 길이 제한 (예: 123456.78 → 9자)
            'maxlength': '9',
            # 정규표현식으로 숫자 입력 형식 제한: 정수부 최대 8자리, 소수점 있을 경우 최대 6자리 정수와 2자리 소숫점
            'pattern': r'^(?:\d{1,8}|\d{1,6}\.\d{1,2})$',
            'title': '가격은 최대 8자리이며, 소수점 이하 두 자리여야 합니다. 예: 12345678 또는 123456.78'
        })
    )
    
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '메뉴 이름을 작성해 주세요.'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '메뉴 설명을 작성해 주세요.'
            }),
            'is_vegan': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')])
        }