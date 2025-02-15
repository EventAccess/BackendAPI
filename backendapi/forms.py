from django import forms



class RegistrationForm(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=100, required=True)
    surname = forms.CharField(label="Surname", max_length=100, required=True)
    discord = forms.CharField(label="Discord", max_length=100, required=True)
    phone = forms.CharField(label="Phone", max_length=100, required=True)
    crew = forms.CharField(label="Crew", max_length=100, required=True)

