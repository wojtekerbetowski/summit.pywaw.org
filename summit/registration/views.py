from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.views.generic import CreateView
from . import models, forms


class AttendeeCreateView(CreateView):
    model = models.Attendee
    form_class = forms.AttendeeForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        self._send_payment_email()
        return response

    def _send_payment_email(self):
        context = {
            'attendee': self.object,
            'site': get_current_site(self.request),
        }
        send_mail(
            subject=render_to_string('emails/registration_subject.txt', context).strip(),
            message=render_to_string('emails/registration_body.txt', context),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.object.email],
        )

