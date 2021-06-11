from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoStatusDogsAppConfig(AppConfig):
    name = "django_cute_status"
    verbose_name = _("django-status-dogs")
