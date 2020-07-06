from django import forms
from bukdjango_captcha.recaptcha_v3.forms import RecaptchaV3Field


class BaseForm(forms.Form):
    recaptcha = RecaptchaV3Field()

