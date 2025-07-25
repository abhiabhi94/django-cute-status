from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _


def http_200(request):
    return HttpResponse(_("OK"))


def http_400(request):
    return HttpResponse(_("Bad request"), status=400)


def http_401(request):
    return HttpResponse(_("Unauthorized"), status=401)


def http_500(request):
    print(an_undefined_variable)  # noqa: F821
