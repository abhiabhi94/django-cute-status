import random

from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.utils.translation import gettext_lazy as _

from django_cute_status.conf import settings


class CuteStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def _get_url(status_code):
        if settings.CUTE_STATUS_USE_RANDOM:
            url = random.choice(settings.CUTE_STATUS_BASE_URLS)
        else:
            url = settings.CUTE_STATUS_BASE_URL
        return url.format(status_code=status_code)

    def _get_response(self, request, status_code):
        try:
            return render(
                request,
                settings.CUTE_STATUS_BASE_TEMPLATE,
                {'cute_status_url': self._get_url(status_code)},
                status=status_code,
            )
        except TemplateDoesNotExist:
            raise ImproperlyConfigured(
                _(
                    'Django Cute Status: The base template for cute status '
                    f'"{settings.CUTE_STATUS_BASE_TEMPLATE}" does not exist.'
                )
            )

    def __call__(self, request):
        response = self.get_response(request)
        status_code = response.status_code

        if (
            settings.CUTE_STATUS_OVERRIDE_HEADER_ON_ALL or
            status_code in settings.CUTE_STATUS_FOR_CODES or
            status_code not in settings.CUTE_STATUS_NOT_FOR_CODES
        ):
            response = self._get_response(request, status_code)
            # header is added after rendering response because the renderer overrides the header.
            response[settings.CUTE_STATUS_HEADER] = self._get_url(status_code)
        return response
