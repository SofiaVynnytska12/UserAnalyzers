# UserAnalyzers

# Kafka Consumer

This Kafka consumer reads user events from the `user_events` topic and prints only the events with allowed types.

## Features

- Consumes and prints events from Kafka.
- Filters events by `event_type`.
- Uses system environment variable `ENABLED_EVENT_TYPES` to control which event types are allowed.

## Event Filtering

You can define which event types should be processed using the `ENABLED_EVENT_TYPES` environment variable.

Example (PowerShell on Windows):

```powershell
$env:ENABLED_EVENT_TYPES = "Click,Login"
python kafka_consumer/consumer.py
```

Default value (if not specified):  
```
Click,Login,Search,Comment
```

## Usage

1. Ensure Kafka is running (`docker-compose up -d`).
2. Run the consumer:
```bash
python kafka_consumer/consumer.py
```
3. Events that match allowed types will be printed to the console.

## Example Output

```
Received allowed event: {'event_type': 'Click', 'user_id': '...', 'timestamp': '...'}
Filtered out event: Search
```
