from django import forms



class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="Enter your name", max_length=100, required=True)
    last_name = forms.CharField(label="Last Name", max_length=100, required=True)
    email = forms.CharField(label="Discord", max_length=100, required=True)
    phone_number = forms.CharField(label="Phone", max_length=100, required=True)
    crew = forms.CharField(label="Crew", max_length=100, required=True)
