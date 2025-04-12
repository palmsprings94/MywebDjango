from django import forms

class Inputletter(forms.Form):
    answer = forms.CharField(max_length=1)
