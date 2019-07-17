# RabbitMQ Python Log Handler

This is a custom log handler for sending python logs to RabbitMQ.

By default messages will be sent to topic 'logs.{domain}.{severity}'
This can be disabled by setting consolidate_levels to true when initialising the handler.

Note that this is a minimal running example for the sake of simplicity (obviously not production code).

### Running
Update the RabbitMQ IP addresses in both example.py and log_listener.py,
run the listener and then start sending logs directly to RabbitMQ!