# core_oaipmh_common_app

core_oaipmh_common_app is a Django app providing basic functionalities for a website.

## Quickstart

  1. Add "core_oaipmh_common_app" to your INSTALLED_APPS setting like this::

  ```python
  INSTALLED_APPS = [
      ...
      'core_oaipmh_common_app',
  ]
  ```

  2. Include the core_oaipmh_common_app URLconf in your project urls.py like this::

  ```python
  url(r'^website/', include('core_oaipmh_common_app.urls')),
  ```

