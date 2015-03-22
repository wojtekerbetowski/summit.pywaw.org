from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import CreateView, DetailView
from . import models, forms


class AttendeeCreateView(CreateView):
    model = models.Attendee
    form_class = forms.AttendeeForm

    def get_success_url(self):
        return self.object.get_absolute_url()

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
            from_email=settings.REGISTRATION_EMAIL,
            recipient_list=[self.object.email],
        )


class AttendeeDetailView(DetailView):
    model = models.Attendee
    slug_url_kwarg = slug_field = 'hash'