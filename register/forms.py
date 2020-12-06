from django.forms import ModelForm
from .models import Developers
from multiselectfield import MultiSelectField
from phone_field import PhoneField
from django import forms
from django.forms.utils import ErrorList

class DeveloperForm(ModelForm):
    error_css_class = 'DivErrorList'
    class Meta:
        model  = Developers
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'first_name', 'style':'margin-bottom:10px; padding:3px;'},) ,
            'last_name':forms.TextInput(attrs={'class':'last_name','style':'margin-bottom:10px; padding:3px;'}),
            'email':forms.EmailInput(attrs={'class':'email_input','style':'margin-bottom:10px; padding:3px;'}),
           
        }

      