from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'country', 'avatar')

        widget = {
            'email': forms.TextInput(attrs={'reandonly': 'reandonly'}),
            'first_name': forms.TextInput(attrs={'reandonly': 'reandonly'}),
            'last_name': forms.TextInput(attrs={'reandonly': 'reandonly'}),
            'phone': forms.TextInput(attrs={'reandonly': 'reandonly'}),
            'country': forms.TextInput(attrs={'reandonly': 'reandonly'}),
        }