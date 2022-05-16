django-cute-status
==================

.. image:: https://github.com/abhiabhi94/django-cute-status/actions/workflows/test.yml/badge.svg?branch=main
    :target: https://github.com/abhiabhi94/django-cute-status/actions
    :alt: Test

.. image:: https://codecov.io/gh/abhiabhi94/django-cute-status/branch/main/graph/badge.svg?token=KBUDpiq2px
    :target: https://codecov.io/gh/abhiabhi94/django-cute-status
    :alt: Coverage

.. image:: https://badge.fury.io/py/django-cute-status.svg
    :target: https://pypi.org/project/django-cute-status/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/django-cute-status.svg
    :target: https://pypi.python.org/pypi/django-cute-status/
    :alt: python

.. image:: https://img.shields.io/pypi/djversions/django-cute-status.svg
    :target: https://pypi.python.org/pypi/django-cute-status/
    :alt: django

.. image:: https://img.shields.io/github/license/abhiabhi94/django-cute-status?color=gr
    :target: https://github.com/abhiabhi94/django-cute-status/blob/main/LICENSE
    :alt: licence


Return a more fun and cute animal picture to your users based upon the HTTP response codes.

Demo Responses
--------------
Some of these responses may look like:

- **404(Resource not found)**

.. image:: https://raw.githubusercontent.com/abhiabhi94/django-cute-status/main/img/404-dog.jpg
    :alt: Resource not found.

- **400(Bad request)**

.. image:: https://raw.githubusercontent.com/abhiabhi94/django-cute-status/main/img/400-cat.jpg
    :alt: Bad request.


Installation
------------

Install using ``pip``.

.. code:: sh

    $ python -m pip install django-cute-status

If you want, you may install it from the source, grab the source code and run ``setup.py``.

.. code:: sh

    $ git clone git://github.com/abhiabhi94/django-cute-status.git
    $ cd django-cute-status
    $ python setup.py install

Usage
-----

Add app
````````

To enable ``django_flag_app`` in your project you need to add it to ``INSTALLED_APPS`` in your projects ``settings.py`` file:

.. code:: python

    INSTALLED_APPS = (
        ...
        'django_cute_status',
        ...
    )

Add middleware
```````````````

Add the following ``middleware`` class to monitor the responses. Make sure it is at the bottom.

.. code:: python

    MIDDLEWARES = [
        ...
        'django_cute_status.middleware.CuteStatusMiddleware',
    ]


Configurations
```````````````

There are certain configurations that allow you to customize the application.

``CUTE_STATUS_BASE_URLS``
~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the list of URLs to be used for displaying cute statuses. At the moment, the app only displays the pictures of dogs and cats. In case you know of any more such services(for e.g. one for pandas) you may add them here. Also, it would be great if you could take a moment to make a pull request to add the feature here as well.
Defaults to :

.. code:: python

     = (
        'https://http.dog/{status_code}.jpg',
        'https://http.cat/{status_code}.jpg',
    )


``CUTE_STATUS_BASE_URL``
~~~~~~~~~~~~~~~~~~~~~~~~~
The default URL for displaying cute statuses. Suppose, you want only cat pictures as status code, you can use this by setting it to ``http://http.cat/{status_code}``. This is useful only when you have set ``CUTE_STATUS_USE_RANDOM`` to ``False``.


``CUTE_STATUS_BASE_TEMPLATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The base template used for rendering cute statuses. It is advisable to override this to cater the web page according to your needs. For example, you might want your header and footer etc. to also be added along the cute status codes. Defaults to ``'django_cute_status/base.html'``.


``CUTE_STATUS_USE_RANDOM``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This tells whether to display cute statuses using one of the available URLs randomly. Defaults to ``True``.


``CUTE_STATUS_FOR_CODES``
~~~~~~~~~~~~~~~~~~~~~~~~~~
This a list of status code for which cute status will be displayed. Defaults to ``(204, 400, 401, 402, 403, 404, 405, 429, 500, 501, 502, 503, 504)``.


``CUTE_STATUS_NOT_FOR_CODES``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a list of status code for which cute status will not be displayed. You may want to display text as per you business logic. Defaults to ``(200, 201, 301, 302, 307, 308)``.


``CUTE_STATUS_HEADER``
~~~~~~~~~~~~~~~~~~~~~~~
This is the header sent added to the response. It can be useful in determining when you want to render your own responses, CSS, JS, media files etc. Defaults to  ``'X-Cute-Status'``.


``CUTE_STATUS_OVERRIDE_HEADER_ON_ALL``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Whether to add the ``CUTE_STATUS_HEADER`` on all HTTP requests or not. Defaults to ``False``.


Credits
-------
The application wouldn't have been possible without the excellent pictures served by https://http.dog and https://http.cat. Many thanks to them for their cute pictures.


Development
-----------
For setting up development environment, you may see the guidelines at `CONTRIBUTING.rst`_.

.. _CONTRIBUTING.rst: https://github.com/abhiabhi94/django-cute-status/tree/main/CONTRIBUTING.rst
