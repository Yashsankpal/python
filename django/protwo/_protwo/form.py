from django import forms
from _protwo.models import User 

class Nameform(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
