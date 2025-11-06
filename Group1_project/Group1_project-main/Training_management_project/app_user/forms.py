from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import User_info

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name',"last_name")

class ExtendProfileForm(forms.ModelForm):
    class Meta:
        model = User_info
        fields = ('student_ID',) 