from django import forms

class IndexForm(forms.Form):
    code = forms.CharField(error_messages={'required': 'Please enter a valid code'},)