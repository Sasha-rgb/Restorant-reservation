from reserv_now.models import HallOne
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = HallOne