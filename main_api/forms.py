from django import forms


class SignUpForm(forms.Form):
    login = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(min_length=8)
