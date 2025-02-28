import re
from rest_framework import serializers
from django.conf import settings
from database.models import Crewmember

# Serializer for the Attendant model: handles validation, serialization, and desersialization of data.
# Change the model later depending on requirements. Please tell me what, and il remake the model later to fit requirements.


class CrewmemberAdmin(serializers.ModelSerializer):  # defined a serialiser class
    first_name = serializers.CharField(
        label=("First Name* "),  # Labels for the field
        required=True,  # This makes the fields required.
        max_length=100,
        style={
            "input_type": "text",
            "autofocus": False,
            "autocomplete": "off",
            "required": True,
        },
        error_messages={
            "required": "This field is required.",
            "blank": "First Name is required.",
        },
    )

    last_name = serializers.CharField(
        label=("Last Name* "),  # Label for the field
        required=True,  # This makes the fields required.
        max_length=100,
        style={
            "input_type": "text",
            "autofocus": False,
            "autocomplete": "off",
            "required": True,
        },
        error_messages={
            "required": "This field is required.",
            "blank": "Last Name is required.",
            "invalid": "Last Name can only contain characters.",
        },
    )

    email = serializers.EmailField(
        label=("Email* "),  # Label for the field
        required=True,  # Field is required
        max_length=100,
        style={
            "input_type": "email",
            "autofocus": False,
            "autocomplete": "off",
            "required": True,
        },
        error_messages={
            "required": "This field is required.",
            "blank": "Email is required.",
        },
    )
    phone_number = serializers.CharField(
        label="Phone Number* ",  # Label for the field
        max_length=14,
        min_length=10,
        required=True,  # Field is required
        error_messages={
            "required": "This field is required .",
            "blank": "Phone number is required.",
        },
    )

    class Meta:
        model = Crewmember
        fields = ["first_name", "last_name", "email", "phone_number"]


def validate_first_name(value):
    # Check if the first name contains only characters or letters with spaces and letters from a-Z
    if not re.match(r"^[a-zA-Zå-öÅ-Ö ]*$", value):
        raise serializers.ValidationError(
            "First Name can only contain letters and spaces."
        )


def validate_last_name(value):
    # Check if the first name contains only characters
    if not re.match(r"^[a-zA-Zå-öÅ-Ö ]*$", value):
        raise serializers.ValidationError(
            "Last Name can only contain letters and spaces."
        )
