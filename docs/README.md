# Collar Metrics Service API
Adheres to [JSON API](http://jsonapi.org/) specification. This means that all
messages will use `application/vnd.api+json` mime type. For the sake of energy
efficiency, devices may choose to queue events locally and deliver them to this
service in batches.

## Bark Events

### POST /collar/:id/bark/new
```json
{
  "data": [{
    "type": "barks",
    "timestamp": "2018-01-14 18:32:01T+0600",
    "volume": 3
  }]
}
```
The objects described in the `data` element will be appended to the collection
of barks known for this device.

### GET /collar/:id/barks
```json
{
  "data": [{
  }]
}
```
Bark events will be delivered in order of timestamp.

## Location Events
