Monitoring plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

This is a Tutor plugin to setup `Grafana <https://grafana.com>`__ for monitoring Docker container stats by using `Prometheus <https://prometheus.io>`__ and `cAdvisor <https://github.com/google/cadvisor>`__. This plugin does not provide support for Kubernetes. This is a beta version of the software and it is not adivsed to be used in production.

This plugin exposes the following endpoints:

* Grafana: http://localhost:3000 (Default username and password is admin)
* Prometheus: http://localhost:9090
* cAdvisor: http://localhost:8080

One `example Grafana dashboard <https://grafana.com/grafana/dashboards/193-docker-monitoring>`__ comes packaged with the plugin.

.. image :: ./docs/resources/GrafanaDashboard.png
    :alt: Grafana Dashboard


Installation
------------

::

    pip install git+https://github.com/ahmed-zubair-1998/tutor-contrib-monitoring

Usage
-----

::

    tutor plugins enable monitoring
    tutor config save

Then you can launch the platform as usual by using one of:

::

    tutor dev start -d
    tutor local start -d

License
-------

This software is licensed under the terms of the AGPLv3.
