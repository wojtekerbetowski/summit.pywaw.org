from django import forms
from . import models


class AttendeeForm(forms.ModelForm):
    accept_terms_of_service = forms.BooleanField(required=True)

    class Meta:
        model = models.Attendee
        fields = (
            'name',
            'tagline',
            'email',
            'twitter',
            'phone',
            'location',
            'display_on_website',
            'notes',
            'invoice',
            'company_name',
            'company_address',
            'company_nip',
            'accept_terms_of_service',
        )