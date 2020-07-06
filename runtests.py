import os
import sys

APP_NAME = "bukdjango_captcha"
APP_DIR = os.path.abspath(os.path.dirname(__file__))

SETTINGS_DICT = {
    "BASE_DIR": APP_DIR,
    "ROOT_URLCONF": f'tests.urls',
    "INSTALLED_APPS": (
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.sites",
            "tests",
            APP_NAME,
        ),
    "DATABASES": {
            "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
        },
    "MIDDLEWARE": (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ),
    "SITE_ID": 1,
    "TEMPLATES": [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [os.path.join(APP_DIR, "tests/templates")],
                "OPTIONS": {
                    "context_processors": [
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                        "django.template.context_processors.tz",
                        "django.contrib.messages.context_processors.messages",
                    ]
                },
            }
        ],
    'LOGGING': {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[{server_time}] {message}',
                'style': '{',
            }
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
            },
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'mail_admins'],
                'level': 'INFO',
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
        }
    },
}


def run_tests():
    import django
    from django.conf import settings
    from django.test.utils import get_runner

    settings.configure(**SETTINGS_DICT)
    django.setup()
    runner = get_runner(settings)

    test_runner = runner(verbosity=3, interactive=True)
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    run_tests()
