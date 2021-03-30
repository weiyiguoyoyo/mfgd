from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from mfgd_app.models import Repository



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
        )


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(help_text=False)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
        

class RepoForm(forms.ModelForm):

	class Meta:
		model = Repository
		fields = (
			"name",
			"path",
			"description",
			"isPublic",
		)

