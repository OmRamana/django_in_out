from django import forms

class VinForm(forms.Form):
    vin_number = forms.CharField()
    