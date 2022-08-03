from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Форма для отправки комментариев к фильму"""
    class Meta:
        model = Review
        fields = ['email', 'name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border',
                'type': 'text',
                'id': 'contactusername',
                'required': '',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border',
                'type': 'text',
                'id': 'contactusername',
                'required': '',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control border',
                'type': 'text',
                'id': 'contactusername',
                'required': '',
            }),
        }