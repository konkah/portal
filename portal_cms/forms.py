from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=20)
    message = forms.CharField(max_length=500)
