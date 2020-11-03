from django import forms
from .models import *

class AddHoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('hood_name', 'hood_photo', 'population')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'neighborhood','email_address')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('business_name', 'email', 'hood')


class Notification(forms.ModelForm):
    class Meta:
        model= Notification
        fields = ('post', 'posted_by', 'hood')