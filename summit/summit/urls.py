from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from registration.views import RegistrationView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^code-of-conduct$', TemplateView.as_view(template_name='code_of_conduct.html'), name='code-of-conduct'),
    url(r'^registration$', RegistrationView.as_view(), name='registration'),
)
