Monitoring plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

This is a Tutor plugin to setup `Grafana <https://grafana.com>`__ for monitoring Docker container stats by using `Prometheus <https://prometheus.io>`__ and `cAdvisor <https://github.com/google/cadvisor>`__. This is a beta version of the software and it is adivsed to be used with caution on production.

This plugin exposes the following endpoints:

Local / Dev:

* Grafana: http://localhost:3000 (Default username and password is admin)
* Prometheus: http://localhost:9090
* cAdvisor: http://localhost:8080

Kubernetes:

* Grafana: http://grafana.{{LMS_HOST}} (Default username and password is admin)
* Prometheus: http://prometheus.{{LMS_HOST}}

A Grafana dashboard is packaged within the plugin.

.. image :: ./docs/resources/GrafanaDashboardDocker.png
    :alt: Grafana Dashboard for Docker containers (Dev and Local)

.. image :: ./docs/resources/GrafanaDashboardK8s.png
    :alt: Grafana Dashboard for Kubernetes cluster


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
    tutor k8s start

Contributions to this repo are welcome

License
-------

This software is licensed under the terms of the AGPLv3.
