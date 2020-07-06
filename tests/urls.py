from django.urls import include, path

urlpatterns = [
    path('recaptcha_v3/', include('tests.test_recaptcha_v3.urls')),
]
