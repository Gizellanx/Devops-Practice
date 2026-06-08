# Day 9 – API Monitoring

## Objective

Learn how Python can be used to monitor APIs and check whether a service is responding correctly.

## What I Did

- Sent requests to an API using Python
- Checked response status codes
- Used conditional logic to determine service health
- Explored how monitoring systems detect service issues

## Key Logic

```python
import requests

response = requests.get("https://api.example.com")

if response.status_code == 200:
    print("Service is healthy")
else:
    print("Service requires investigation")
```

The script sends a request to an API and checks the response code. If the service responds successfully, it is considered healthy. Any other response may indicate an issue that requires investigation.

## Example Output

```plaintext
Service is healthy
```

## What I Learned

- How APIs allow systems to communicate with each other
- How Python can send requests to external services
- Why response codes are important for monitoring
- How API monitoring helps identify service issues

## Next Improvements

- Monitor multiple APIs
- Record response times
- Save monitoring results to a log file
- Generate alerts when services become unavailable

## Key Takeaway

Many monitoring tools rely on APIs. Understanding how to check API responses in Python provides a foundation for automation, monitoring, and troubleshooting workflows.
