# this is added here for easy override to a new vendor in case this service is no longer available
import os


CUTE_STATUS_BASE_URLS = (
    'https://httpstatusdogs.com/img/{status_code}.jpg',
    'https://http.cat/{status_code}.jpg',
)

CUTE_STATUS_BASE_URL = CUTE_STATUS_BASE_URLS[0]

CUTE_STATUS_USE_RANDOM = True

CUTE_STATUS_FOR_CODES = (
    204,
    400,
    401,
    402,
    403,
    404,
    500,
)

CUTE_STATUS_NOT_FOR_CODES = (
    200,
    201,
    301,
    302,
)

CUTE_STATUS_HEADER = 'X-Cute-Status'

CUTE_STATUS_OVERRIDE_HEADER_ON_ALL = False

CUTE_STATUS_BASE_TEMPLATE = os.path.join('django_cute_status', 'base.html')
