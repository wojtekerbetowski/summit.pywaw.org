from django import forms
from . import models


class AttendeeForm(forms.ModelForm):
    accept_terms_of_service = forms.BooleanField(required=True)

    class Meta:
        model = models.Attendee