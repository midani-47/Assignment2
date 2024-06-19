from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= CustomUser
        fields= ('username', 'email', 'password1', 'password2')


    def clean_email(self):
        email=self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def clean_username(self):
        username=self.cleaned_data.get('username')
        if CustomUser.objects.filter(username= username).exists():
            raise forms.ValidationError("A user with that username already exists.")
        return username


# User = get_user_model()


# class UserRegisterForm(UserCreationForm):
#     email=forms.EmailField()
#
#     class Meta:
#         model= User
#         fields= ['username', 'email', 'password1', 'password2']
