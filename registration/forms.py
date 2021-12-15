from django import forms
from django.contrib.auth.forms import *
from.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class Createuserform(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']