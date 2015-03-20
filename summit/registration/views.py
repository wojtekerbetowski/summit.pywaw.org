from django.views.generic import CreateView
from . import models, forms


class RegistrationView(CreateView):
    model = models.Attendee
    form_class = forms.AttendeeForm
    template_name = 'registration.html'