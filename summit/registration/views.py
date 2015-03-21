from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import models, forms


class AttendeeCreateView(CreateView):
    model = models.Attendee
    form_class = forms.AttendeeForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home')