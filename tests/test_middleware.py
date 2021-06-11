import pytest
from django.core.exceptions import ImproperlyConfigured

from django_cute_status.conf import settings


def _mock_random(_):
    return settings.CUTE_STATUS_BASE_URL


def test_header_override_all(client, monkeypatch):
    monkeypatch.setattr(settings, 'CUTE_STATUS_OVERRIDE_HEADER_ON_ALL', True)
    monkeypatch.setattr('django_cute_status.middleware.random.choice', _mock_random)

    response = client.get('/')

    assert response.status_code == 200
    assert response.has_header('X-Cute-Status') is True
    assert response['X-Cute-Status'] == 'https://httpstatusdogs.com/img/200.jpg'


def test_not_allowed_codes(client, monkeypatch):
    response = client.get('/')

    assert response.status_code == 200
    assert response.has_header('X-Cute-Status') is False


def test_random_disabled(client, monkeypatch):
    monkeypatch.setattr(settings, 'CUTE_STATUS_USE_RANDOM', False)

    response = client.get('/400/')

    assert response.status_code == 400
    assert response.has_header('X-Cute-Status') is True
    # this is the default url to be used
    assert response['X-Cute-Status'] == 'https://httpstatusdogs.com/img/400.jpg'


def test_allowed_code(client, monkeypatch):
    monkeypatch.setattr('django_cute_status.middleware.random.choice', _mock_random)

    response = client.get('/400/')

    assert response.status_code == 400
    assert response.has_header('X-Cute-Status') is True
    assert response['X-Cute-Status'] == 'https://httpstatusdogs.com/img/400.jpg'

    assert response.context['cute_status_url'] == 'https://httpstatusdogs.com/img/400.jpg'


def test_base_template_does_not_exist(client, monkeypatch):
    monkeypatch.setattr(settings, 'CUTE_STATUS_BASE_TEMPLATE', 'does_not_exist.html')

    with pytest.raises(ImproperlyConfigured) as err:
        client.get('/400/')

    assert str(err.value) == (
        'Django Cute Status: The base template for cute status "does_not_exist.html" does not exist.'
    )
