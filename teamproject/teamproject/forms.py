from django import forms

class Email(forms.Form):
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
