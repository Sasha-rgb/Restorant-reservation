from django.contrib.auth.models import User
from registration.models import User, UserProfile
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password", "email")


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ("picture",)