from django import forms
from .models import Attendant  # Import your model

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Attendant  # Link the form to the Attendant model
        fields = [
            'first_name',
            'last_name',
            'email',
            'discord',
            'phone_number',
            'crew',
            'ticketCrewID',
            'profile_image'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-input", "placeholder": "Ola"}),
            'last_name': forms.TextInput(attrs={"class": "form-input", "placeholder": "Nordmann"}),
            'email': forms.EmailInput(attrs={"class": "form-input", "placeholder": "example@email.com"}),
            'discord': forms.TextInput(attrs={"class": "form-input", "placeholder": "Discord#1234"}),
            'phone_number': forms.TextInput(attrs={"class": "form-input", "placeholder": "+123456789"}),
            'crew': forms.TextInput(attrs={"class": "form-input", "placeholder": "Enter your crew name"}),
            'ticketCrewID': forms.TextInput(attrs={"class": "form-input", "placeholder": "Ticket ID", "disabled": True}),
}
    ticketCrewID = forms.CharField(required=False)



