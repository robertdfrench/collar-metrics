# Collar Metrics Service API
Adheres to [JSON API](http://jsonapi.org/) specification. This means that all
messages will use `application/vnd.api+json` mime type. For the sake of energy
efficiency, devices may choose to queue events locally and deliver them to this
service in batches.

## Bark Events

### POST /collar/:id/barks/new
```json
{
  "data": [{
    "type": "barks",
    "attributes": {
      "timestamp": "2018-01-14 18:32:01T+0600",
      "volume": 3
    }
  }]
}
```
The objects described in the `data` element will be appended to the collection
of barks known for this device.

### GET /collar/:id/barks
```json
{
  "data": [{
    "type": "barks",
    "attributes": {
      "timestamp": "2018-01-14 18:32:01T+0600",
      "volume": 3
    }
  },{
    "type": "barks",
    "attributes": {
      "timestamp": "2018-01-14 18:32:04T+0600",
      "volume": 5
    }
  }]
}
```
Bark events will be delivered in order of timestamp.

## Location Events

### POST /collar/:id/locations/new
```json
{
  "data": [{
    "type": "locations",
    "attributes": {
      "lat": 36.0103,
      "lon": -84.2696,
      "timestamp": "2018-01-14 18:32:04T+0600"
    }
  }]
}
```

### GET /collar/:id/locations
```json
{
  "data": [{
    "type": "locations",
    "attributes": {
      "lat": 36.0103,
      "lon": -84.2696,
      "timestamp": "2018-01-14 18:32:04T+0600"
    }
  }]
}
```

## Physical Activity

### POST /collar/:id/physical-activity/new
```json
{
  "data": [{
    "type": "physical-activity",
    "attributes": {
      "heart-rate": 110,
      "temp": 101.2,
      "timestamp": "2018-01-14 18:32:04T+0600"
    }
  }]
}
```

### GET /collar/:id/physical-activity
```json
{
  "data": [{
    "type": "physical-activity",
    "attributes": {
      "heart-rate": 110,
      "temp": 101.2,
      "timestamp": "2018-01-14 18:32:04T+0600"
    }
  }]
}
```
