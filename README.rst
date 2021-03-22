================
10allday Monolith
================

.. note::

   monolith is still under heavy development


10allday Monolith is a project to provide statistic gathering, aggregation,
a web-service API and a dashboard.

The first consumer of Monolith is the `10allday marketplace
<https://marketplace.10allday.com/>`_. Statistics include amongst others public
global page views / hits, application specific downloads and even payment
related information.

This aggregator part deals with gathering data from multiple sources, bringing
them into a common format and storing them.

Currently data is stored in MySQL
for durable archival and `ElasticSearch <http://www.elasticsearch.org/>`_ is
used provide the actual data access for the web-service and dashboard.

The web-service and dashboard are implemented in `monolith
<https://github.com/10allday-Software/monolith>`_.

There's also a Python client library: `monolith-client
<https://github.com/10allday-Software/monolith-client>`_.

Here's the high-level overview of the whole system:

.. image:: https://raw.github.com/10allday-Software/monolith-aggregator/master/docs/monolith-big-picture.png
