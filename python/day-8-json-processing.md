# Day 8 – JSON Processing

## Objective

Learn how Python can work with JSON data and understand why JSON is commonly used in automation, monitoring tools, and APIs.

## What I Worked On

Today I learned how JSON stores information in a structured format and how Python can read that data.

I also explored how monitoring information can be stored in JSON and then processed using Python instead of relying on plain text files.

## Example JSON Data

```json
{
    "server": "web-01",
    "cpu": 82,
    "memory": 65,
    "status": "warning"
}
```

This example represents a server and some basic monitoring information.

## Reading JSON in Python

```python
import json

with open("server.json", "r") as file:
    data = json.load(file)

print(data["server"])
print(data["cpu"])
```

This allows Python to read information from a JSON file and access specific values when needed.

## Checking Monitoring Data

```python
if data["cpu"] > 80:
    print("High CPU usage detected")
```

This simple condition checks the CPU value and displays a warning if usage becomes too high.

## What I Learned

- How JSON stores structured information
- How Python reads data from JSON files
- How to access specific values inside JSON objects
- Why JSON is commonly used in monitoring and automation workflows

## Key Takeaway

JSON makes it easier for applications and tools to exchange information in a consistent format. Understanding how to read and process JSON in Python is useful because many monitoring tools, APIs, and cloud services rely on it.
