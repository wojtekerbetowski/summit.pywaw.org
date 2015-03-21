from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    email = models.EmailField()
    twitter = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    display_on_website = models.BooleanField(default=True)
    notes = models.TextField()
    invoice = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=500)
    company_nip = models.CharField(max_length=10)
    is_paid = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
