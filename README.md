Python Services Sample
=====================

This sample is built for Shippable, a docker based continuous integration and deployment platform.

**CouchDB:**

Uses couchdbkit to test simple document insertion on a CouchDB instance.

This sample project will fail when built with python 3.x. 

The couchdbkit package used in this project does not support python 3.x.

http://couchdbkit.org/download.html


**RabbitMQ:**

Tests RabbitMQ via the Pika library.


**ElasticSearch:**

This sample will fail when built with python 3.2. pyes package has used a syntax that is not supported by python 3.2. https://github.com/shippableSamples/sample_python_elasticsearch/issues/3 http://stackoverflow.com/questions/2464959/whats-the-u-prefix-in-a-python-string


**Memcache:**

Tests memcache.


**Redis:**

Tests redis.
