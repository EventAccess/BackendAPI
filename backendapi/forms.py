from django import forms
from database.models import Attendant, Crewmember, Crews


class AttendantNFCForm(forms.ModelForm):
    prefix = "attendant"

    class Meta:
        model = Attendant
        fields = [
            "nfc_id",
        ]
        widgets = {
            "nfc_id": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Scan NFC tag...",
                    # "disabled": True,
                }
            ),
        }


class CrewmemberForm(forms.ModelForm):
    # Allow multiple (different) forms in single page
    # Can also be specified as an argument to the class init
    prefix = "crewmember"

    class Meta:
        model = Crewmember  # Link the form to the Attendant model
        fields = [
            "first_name",
            "last_name",
            "email",
            "discord",
            "phone_number",
            "crew",
            "profile_image",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Ola"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nordmann"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-input", "placeholder": "email@example.com"}
            ),
            "discord": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Discord#1234"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "+47012345678"}
            ),
            "crew": forms.TextInput(
                # Crews.objects.all(),
                attrs={"class": "form-input", "placeholder": "Select crew..."},
            ),
        }
