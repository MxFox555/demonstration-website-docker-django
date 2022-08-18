from django import forms
from web.models import UserAPI, AccountType
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'name': 'username',
            'type': 'username',
            'autofocus': '',
            }), max_length=100)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'E-mail',
            'name': 'email',
            'type': 'email',
            'autofocus': '',
            }), max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'name': 'password',
            'type': 'password',
            'value': '',
        }), max_length=100)
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'onchange': "CheckPassword('password', 'confirm_password', 'confirm-password-wrapper', 'password-confirm-error', 'signup-button')",
            'class': 'form-control',
            'placeholder': 'Re-enter Password',
            'name': 'confirm_password',
            'type': 'password',
            'value': '',
        }), max_length=100)
    checkbox = forms.BooleanField(widget=forms.CheckboxInput(attrs={
            'name': 'termsandconditions',
            'type': 'checkbox',
            'value': 'True',
        }))
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def make_api_key(self):
        key = get_random_string(length=30)
        #print(UserAPI.objects.filter(username='admin'))
        while len(UserAPI.objects.filter(api_key=key)) >= 1:
            key = get_random_string(length=30)
        #print(key)
        return key

    def make_activate_key(self):
        key = get_random_string(length=100)
        #print(UserAPI.objects.filter(username='admin'))
        while len(UserAPI.objects.filter(activate_key=key)) >= 1:
            key = get_random_string(length=100)
        #print(key)
        return key

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.api_key = self.make_api_key()
        user.activate_key = self.make_activate_key()
        user.account_type = AccountType.objects.get(type_name='Free')
        user.is_active = False
        #print(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'name': 'username',
            'type': 'username',
            'autofocus': '',
            }), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'name': 'password',
            'type': 'password',
            'value': '',
        }), max_length=100)

class ForgotPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'E-mail',
            'name': 'email',
            'type': 'email',
            'autofocus': '',
            }), max_length=100)

class ResetPasswordWithKey(forms.Form):
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