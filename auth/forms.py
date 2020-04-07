from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Email"
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))


class SignupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Name"
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Email"
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(username=email)
        if qs.exists():
            raise forms.ValidationError("Email already registered")

        return email

    def clean(self):
        data = self.cleaned_data
        password = data['password']
        password2 = data['password2']
        if password != password2:
            raise forms.ValidationError("Password didn't match")
        return data
