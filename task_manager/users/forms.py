from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        user_email = kwargs.pop('user_email', None)
        super().__init__(*args, **kwargs)
        if user_email:
            self.fields['email'].initial = user_email
            self.fields['email'].widget.attrs['readonly'] = True