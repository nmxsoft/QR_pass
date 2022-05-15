from django import forms

from .models import Customer


class PassForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = (
            'username', 'real_name', 'access'
        )
