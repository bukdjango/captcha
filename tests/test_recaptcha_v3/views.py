from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import BaseForm


class RecaptchaV3View(FormView):
    template_name = 'test_recaptcha_v3/index.html'
    form_class = BaseForm

    def get_success_url(self):
        return self.request.path
