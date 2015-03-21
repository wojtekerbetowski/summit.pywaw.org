from djet.assertions import EmailAssertionsMixin, StatusCodeAssertionsMixin
from djet.testcases import ViewTestCase
from . import views, models


class AttendeeCreateViewTest(ViewTestCase, EmailAssertionsMixin, StatusCodeAssertionsMixin):
    view_class = views.AttendeeCreateView

    def test_post_should_create_attendee_and_send_payment_info(self):
        data = {
            'name': 'John Lennon',
            'tagline': 'Guitar Master',
            'email': 'john@lenon.com',
            'twitter': '@johnlennon',
            'phone': '123123123',
            'location': 'London, UK',
            'display_on_website': True,
            'invoice': True,
            'company_name': 'The Beatles',
            'company_address': 'Main St, London, UK',
            'company_nip': '123123123',
            'accept_terms_of_service': True,
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        attendee = models.Attendee.objects.get(email=data['email'])
        self.assert_redirect(response, attendee.get_absolute_url())
        self.assert_emails_in_mailbox(1)
        self.assert_email_exists(to=[data['email']])
