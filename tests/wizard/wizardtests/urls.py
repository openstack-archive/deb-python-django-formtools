from django.conf.urls import url

from .forms import (
    CookieContactWizard, Page1, Page2, Page3, Page4, SessionContactWizard,
)

urlpatterns = [
    url(r'^wiz_session/$', SessionContactWizard.as_view(
        [('form1', Page1),
         ('form2', Page2),
         ('form3', Page3),
         ('form4', Page4)])),
    url(r'^wiz_cookie/$', CookieContactWizard.as_view(
        [('form1', Page1),
         ('form2', Page2),
         ('form3', Page3),
         ('form4', Page4)])),
    url(r'^wiz_other_template/$', CookieContactWizard.as_view(
        [('form1', Page1),
         ('form2', Page2),
         ('form3', Page3),
         ('form4', Page4)],
        template_name='other_wizard_form.html')),
]
