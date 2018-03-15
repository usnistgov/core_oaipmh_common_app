======================
Core Oaipmh Common App
======================

Base OAI-PMH sharing functions for the curator core project.

Quickstart
==========

1. Add "core_oaipmh_common_app" to your INSTALLED_APPS setting
--------------------------------------------------------------

.. code:: python

    INSTALLED_APPS = [
      ...
      'core_oaipmh_common_app',
    ]

2. Include the core_oaipmh_common_app URLconf in your project urls.py
---------------------------------------------------------------------

.. code:: python

    url(r'^oaipmh/', include('core_oaipmh_common_app.urls')),
