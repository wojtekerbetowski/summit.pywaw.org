from django.contrib import admin
from . import models


class AttendeeModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'location',
        'invoice',
        'is_paid',
        'registration_date',
    )
    readonly_fields = ('registration_date',)

admin.site.register(models.Attendee, AttendeeModelAdmin)
