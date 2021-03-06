from django import forms
from .models import Profile


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'gender', 'country', 'bio', 'avatar',)


class SearchForm(forms.Form):
    query = forms.CharField()
