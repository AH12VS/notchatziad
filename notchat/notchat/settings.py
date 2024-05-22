# ========== IMPORTS ========== #
import os
from pathlib import Path
from dotenv import load_dotenv
from django.contrib import messages

# ========== ENDIMPORTS ========== #


# ========== ENV ========== #
load_dotenv()
# ========== ENDENV ========== #


# ========== BASEDIR ========== #
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# ========== ENDBASEDIR ========== #


# ========== SECURE ========== #
SECRET_KEY = os.environ.get("SECRET_KEY")
# ========== ENDSECURE ========== #


# ========== DEBUG ========== #
DEBUG = os.environ.get("DEBUG") == "True"
# ========== ENDDEBUG ========== #


# ========== HOSTS ========== #
ALLOWED_HOSTS = ["*"]
# ========== ENDHOSTS ========== #


# ========== APPS ========== #
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    #
    "daphne",
    "channels",
    #
    "django.contrib.staticfiles",
]

APPS = [
    "users.apps.UsersConfig",
    "home.apps.HomeConfig",
    "signin.apps.SigninConfig",
    "signout.apps.SignoutConfig",
    "signup.apps.SignupConfig",
    "about.apps.AboutConfig",
    "copyr.apps.CopyrConfig",
    "errhandlers.apps.ErrhandlersConfig",
    "rooms.apps.RoomsConfig",
    "search.apps.SearchConfig",
]

INSTALLED_APPS = DJANGO_APPS + APPS
# ========== ENDAPPS ========== #


# ========== MIDDLEWARE ========== #
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# ========== ENDMIDDLEWARE ========== #


# ========== URLCONF ========== #
ROOT_URLCONF = "notchat.urls"
# ========== ENDURLCONF ========== #


# ========== TEMPLATES ========== #
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
# ========== ENDTEMPLATES ========== #


# ========== WSGI ========== #
WSGI_APPLICATION = "notchat.wsgi.application"
# ========== ENDWSGI ========== #


# ========== ASGI ========== #
ASGI_APPLICATION = "notchat.asgi.application"
# ========== ENDASGI ========== #


# ========== CHANNEL ========== #
CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
# ========== ENDCHANNEL ========== #


# ========== DB ========== #
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# ========== ENDDB ========== #


# ========== AUTH ========== #
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
# ========== ENDAUTH ========== #


# ========== INTERNATIONALIZATION ========== #
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"
TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True
# ========== ENDINTERNATIONALIZATION ========== #


# ========== MESSAGES ========== #
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}
# ========== ENDMESSAGES ========== #


# ========== USER ========== #
AUTH_USER_MODEL = "users.UserModel"
# ========== ENDUSER ========== #


# ========== STATIC ========== #
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "static/"
STATIC_ROOT = "staticfiles/"
STATICFILES_DIRS = [BASE_DIR / "static"]
# ========== ENDSTATIC ========== #


# ========== MEDIA ========== #
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# ========== ENDMEDIA ========== #


# ========== PK ========== #
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# ========== ENDPK ========== #


# ========== LOGGING ========== #
LOGGING = {
    "version": 1,
    "loggers": {
        "django": {
            # "handlers": ["file", "console", "debughandler"],
            "handlers": ["file", "console"],
            "level": "DEBUG",
        }
    },
    "handlers": {
        "file": {
            "level": "INFO",  # level set to INFO to just save useful logs
            "class": "logging.FileHandler",
            "filename": "./logs/logs.log",
            "formatter": "fileformatter",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "consoleformatter",
        },
        # "debughandler": {
        #     "level": "DEBUG",  # level set to DEBUG to save all logs
        #     "class": "logging.FileHandler",
        #     "filename": f"{USER_WORK_SPACE}/logs/sch/debug.log",
        #     # "filename": "./logs/debug.log",
        #     "formatter": "fileformatter",
        # },
    },
    "formatters": {
        "fileformatter": {
            # "format": "*** \n[{asctime}] ||| {levelname} ||| {name} ||| {module} ||| {message} \n***",
            "format": "<<<[{asctime}]  [{levelname}]  [{module}]  [{message}]>>>",
            "style": "{",
        },
        "consoleformatter": {
            "format": "***\n[{asctime}]  [{levelname}]  [{message}]\n***",
            "style": "{",
        },
    },
}
# ========== ENDLOGGING ========== #


# ========== COOKIE ========== #
SESSION_COOKIE_AGE = 864000
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# ========== ENDCOOKIE ========== #


# ========== HSTS ========== #
# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# ========== ENDHSTS ========== #


# ========== SECUREREDIRECT ========== #
# SECURE_SSL_REDIRECT = True
# ========== ENDSECUREREDIRECT ========== #


# ========== XSSPROTECTION ========== #
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# ========== ENDXSSPROTECTION ========== #
