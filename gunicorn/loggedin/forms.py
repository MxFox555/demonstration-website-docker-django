from django import forms
from django.contrib.auth import get_user_model

class InformationUsernameForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'name': 'username',
            'type': 'text',
            'value': '{{ user.username }}',
            }), max_length=100)

class PasswordUpdateForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Current password',
            'name': 'old_password',
            }), max_length=100)
    new_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'New password',
            'name': 'new_password',
            }), max_length=100)
    new_password_confirm = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm new password',
            'name': 'new_password_confirm',
            }), max_length=100)
    
