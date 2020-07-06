from django.test import TestCase
from .forms import BaseForm
import os


class RecaptchaV3TestCase(TestCase):

    def test_form_invalid(self):
        form = BaseForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('recaptcha', form.errors.keys())
        self.assertEqual(['Are you a robot?'], form.errors['recaptcha'])

    def test_form_valid_when_disabled(self):
        os.environ["BUKDJANGO_CAPTCHA_RECAPTCHA_V3_DISABLE"] = "1"
        form = BaseForm(data={})
        self.assertTrue(form.is_valid())
