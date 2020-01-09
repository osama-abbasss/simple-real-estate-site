from django import forms
from .models import ReserveProperty


class ReserveFrom(forms.ModelForm):

    class Meta:
        model = ReserveProperty
        fields = ['first_name','last_name','email','message']
