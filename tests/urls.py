from django.urls import path

from tests.views import http_200
from tests.views import http_400
from tests.views import http_401
from tests.views import http_500


app_name = 'tests'

urlpatterns = [
    path('', http_200, name='200',),
    path('400/', http_400, name='400',),
    path('401/', http_401, name='401',),
    path('500/', http_500, name='500',),
]
