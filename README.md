![build status](https://api.travis-ci.org/robertdfrench/collar-metrics.svg?branch=master)

# Collar-metrics
Proof of Concept IoT metrics collection service

* [API Documentation](https://robertdfrench.github.io/collar-metrics/)

### Live Demo
I chose to track bark events associated emitted from each collar on the
assumption that collars have a globally unique id. Here we have bark data for
two collars:

* [Collar 1](https://wl0r0tyko5.execute-api.us-east-1.amazonaws.com/production/collar/1/barks)
* [Collar 2](https://wl0r0tyko5.execute-api.us-east-1.amazonaws.com/production/collar/2/barks)

#### Adding Bark Data
You can simulate a bark event from the command line as follows:

```bash
curl -H "Content-Type: application/json" -X POST --data '{"data": [{"type": "barks", "attributes": {"timestamp": "2018-05-11 03:05:50", "volume": 7}}]}' https://wl0r0tyko5.execute-api.us-east-1.amazonaws.com/production/collar/2/barks/new
```

Feel free to play around with the timestamp, bark volume, and collar id.

### Design Notes
Everything is managed through the `Makefile` -- deployment, the development
environment, and the test pipeline. Though it is a controversial choice, I
imposed 100% test coverage on the `collar_metrics` package because it forces
a more rigorous design; `app.py` and `migrate.py` are omitted from this because
they contain no substatial logic, by design. The API is organized around the
[JSON API](http://jsonapi.org/) spec for no other reason than it keeps me from
fretting about how things should look.
