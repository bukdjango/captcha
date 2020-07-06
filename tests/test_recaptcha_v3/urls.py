from django.urls import path

from .views import RecaptchaV3View

urlpatterns = [
    path('', RecaptchaV3View.as_view())
]
