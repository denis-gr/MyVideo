from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-lgy3o#uy#8-g7z!q&zj$q&xrx5)os^k7dfnz*5+rc94xnqdgja"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["https://*.gitpod.io/"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

#CORS_ALLOWED_ORIGINS = [
#    'https://5173-denisgr-myvideofront-cne3wanp45m.ws-eu89.gitpod.io',
#]

try:
    from .local import *
except ImportError:
    pass
