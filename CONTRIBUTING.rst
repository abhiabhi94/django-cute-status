==================================
Contributing to Django Cute Status
==================================

There are many ways to contribute to the project. You may improve the documentation, address a bug, add some feature to the code or do something else. All sort of contributions are welcome.


Development
-----------

To start development on this project, you may fork this repository and follow the following guidelines.

.. code:: sh

    # clone the forked repository
    $ git clone YOUR_FORKED_REPO_URL

    # create a virtual environment
    $ python3 -m venv venv
    # activate the virtual environment(unix users)
    $ . venv/bin/activate
    # activate the virtual environment(window users)
    $ venv\Scripts\activate
    # install dependencies
    (venv) $ pip install -e . Django -r dev-requirements.txt pre-commit
    # migrate the migrations to the database
    # in case you want to view the status on the browser
    (venv) $ python -m django runserver --settings=test.settings


Testing
-------

To run tests against a particular ``python`` and ``django`` version installed inside your virtual environment, you may use:

.. code:: sh

    (venv) $ pytest

To run tests against all supported ``python`` and ``django`` versions, you may run:

.. code:: sh

    # install dependency
    (venv) $ pip install tox
    # run tests
    (venv) $ tox
