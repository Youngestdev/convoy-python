# convoy-python
Convoy SDK for Python

This is the Convoy Python SDK. This SDK contains methods for easily interacting with Convoy's API. Below are examples to get you started. For additional examples, please see our official documentation at (https://convoy.readme.io/reference)


## Installation
Install convoy-python with

```bash
pip install convoy-python
```

## Setup Client
Next, import the `convoy` module and setup with your auth credentials.

```python
from convoy import Convoy
convoy = Convoy({"api_key":"your_api_key"})
```
The SDK also supports authenticating via Basic Auth by defining your username and password.

```python
convoy = Convoy({"username":"default", "password":"default"})
```

In the event you're using a self hosted convoy instance, you can define the url as part of what is passed into convoy's constructor.

```python
convoy = Convoy({ "api_key": 'your_api_key', "uri": 'self-hosted-instance' })
```

## Usage

### Get all groups

```python
(response, status) = convoy.group.all({ "perPage": 10, "page": 1 })
```

### Creating an Application

An application represents a user's application trying to receive webhooks. Once you create an application, you'll receive a `uid` that you should save and supply in subsequent API calls to perform other requests such as creating an event.

```python
appData = { "name": "my_app", "support_email": "support@myapp.com" }
(response, status)  = convoy.application.create({}, appData)
app_id = response["data"]["uid"]

```

### Add Application Endpoint

After creating an application, you'll need to add an endpoint to the application you just created. An endpoint represents a target URL to receive events.

```python
endpointData = {
    "url": "https://0d87-102-89-2-172.ngrok.io",
    "description": "Default Endpoint",
    "secret": "endpoint-secret",
    "events": ["*"],
  }

(response, status) = convoy.endpoint.create(app_id, {}, endpointData)
```

### Sending an Event

To send an event, you'll need the `uid` we created in the earlier section.

```python
eventData = {
    "app_id": app_id,
    "event_type": "payment.success",
    "data": {
      "event": "payment.success",
      "data": {
        "status": "Completed",
        "description": "Transaction Successful",
        "userID": "test_user_id808",
      },
    },
  }

(response, status) = convoy.event.create({}, eventData)
```

## Testing

```python
pytest ./test/test.py
```

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.MD) for details.


## Credits

- [Frain](https://github.com/frain-dev)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
