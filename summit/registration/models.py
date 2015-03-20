from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    email = models.EmailField()
    twitter = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    display_on_website = models.BooleanField()
    notes = models.TextField()
    invoice = models.BooleanField()
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=500)
    nip = models.CharField(max_length=20)
